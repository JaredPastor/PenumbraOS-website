#!/usr/bin/env python3
"""
Convert clean_articles JSON files to Hugo content Markdown files.
Reads from ../support/clean_articles/ and writes to site/content/knowledgebase/
"""

import json
import os
import re
import html
from pathlib import Path
from datetime import datetime

# Section ID -> human-readable section name mapping
# Derived from the original Zendesk category/section structure
SECTION_MAP = {
    # Power & Charging
    22616709355149: {"name": "Power & Charging", "category": "Ground Control", "weight": 10},
    30079786216589: {"name": "Power & Charging", "category": "Ground Control", "weight": 10},
    24719118093069: {"name": "Power & Charging", "category": "Ground Control", "weight": 10},

    # Features & Usage
    24192735950861: {"name": "Features & Usage", "category": "Ground Control", "weight": 20},
    24192749929997: {"name": "Features & Usage", "category": "Ground Control", "weight": 20},
    22969025694477: {"name": "Features & Usage", "category": "Ground Control", "weight": 20},
    30751243857165: {"name": "Features & Usage", "category": "Ground Control", "weight": 20},

    # Communication & Contacts
    22616723137805: {"name": "Communication & Contacts", "category": "Ground Control", "weight": 30},

    # Media & Data
    25293321386253: {"name": "Media & Data", "category": "Ground Control", "weight": 40},

    # Connectivity & Travel
    22968771221645: {"name": "Connectivity & Travel", "category": "Ground Control", "weight": 50},

    # Account & Billing
    22968808982541: {"name": "Account & Billing", "category": "Ground Control", "weight": 60},
    25050527005709: {"name": "Account & Billing", "category": "Ground Control", "weight": 60},

    # Safety & Recalls
    22968788577549: {"name": "Safety & Recalls", "category": "Ground Control", "weight": 70},

    # Maintenance
    30092452654477: {"name": "Maintenance", "category": "Ground Control", "weight": 80},
}

DEFAULT_SECTION = {"name": "General", "category": "Ground Control", "weight": 90}

# Set of valid article slugs (populated at startup by main())
# Used by clean_html_body() to detect links to unrecovered articles
VALID_SLUGS = set()


def slugify(title):
    """Convert article title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def clean_unicode(text):
    """Clean unrenderable Unicode characters from text.

    - Replaces non-breaking spaces (U+00A0, U+202F) with regular spaces
    - Removes Private Use Area characters (U+E000–U+F8FF) — icon font glyphs
      from Humane's proprietary "AiPin Symbols VF" font that render as blank
      boxes/tofu without the font
    """
    if not text:
        return text
    text = text.replace('\u00A0', ' ')
    text = text.replace('\u202F', ' ')
    text = re.sub(r'[\uE000-\uF8FF]', '', text)
    return text


def clean_html_body(body):
    """Clean up Zendesk-specific HTML in article bodies."""
    if not body:
        return ""

    # Rewrite image URLs to use local media paths
    # Pattern: src="https://support.humane.com/hc/article_attachments/NNNNN"
    body = re.sub(
        r'src="https://support\.humane\.com/hc/article_attachments/(\d+)"',
        r'src="/media/\1.png"',
        body
    )

    # Also handle already-rewritten paths from articles_final
    body = re.sub(
        r'src="media/(\d+)\.\w+"',
        r'src="/media/\1.png"',
        body
    )

    # Rewrite internal article links to use our local paths
    def rewrite_article_link(match):
        article_id = match.group(1)
        slug_part = match.group(2)
        new_slug = slug_part.lower()
        return f'href="/knowledgebase/{new_slug}/"'

    body = re.sub(
        r'href="https://support\.humane\.com/hc/en-us/articles/(\d+)-([^"]+)"',
        rewrite_article_link,
        body
    )

    # Convert links to unrecovered articles into plain text
    # After rewriting, internal links look like: <a href="/knowledgebase/SLUG/">text</a>
    def strip_dead_link(match):
        slug = match.group(1)
        inner_text = match.group(2)
        if slug not in VALID_SLUGS:
            return inner_text  # Just the text, no link
        return match.group(0)  # Keep valid links as-is

    body = re.sub(
        r'<a[^>]*href="/knowledgebase/([^/"]+)/"[^>]*>(.*?)</a>',
        strip_dead_link,
        body,
        flags=re.DOTALL
    )

    # Strip ALL inline style attributes (both populated and empty)
    # These come from Zendesk/Tailwind and are massive bloat
    body = re.sub(r'\s*style="[^"]*"', '', body)

    # Also handle single-quoted style attributes just in case
    body = re.sub(r"\s*style='[^']*'", '', body)

    # Strip data-* attributes
    body = re.sub(r'\s*data-[\w-]+="[^"]*"', '', body)

    # Strip dir attributes
    body = re.sub(r'\s*dir="[^"]*"', '', body)

    # Remove Tailwind/ChatGPT wrapper divs — these are Zendesk chat widget
    # artifacts that wrap normal content in deeply nested divs with Tailwind classes.
    # We strip the opening and closing div tags but keep inner content.
    # Match divs whose class contains Tailwind utility classes
    tailwind_classes = [
        'flex', 'text-message', 'markdown', 'prose', 'dark:prose-invert',
        'items-center', 'gap-', 'rounded-xl', 'empty:hidden', 'break-words',
        'whitespace-normal', 'flex-col', 'flex-grow', 'w-full', 'min-h-',
        'justify-start', 'mb-2', '-ml-2'
    ]
    tailwind_pattern = '|'.join(re.escape(c) for c in tailwind_classes)
    # Remove opening div tags with Tailwind classes
    body = re.sub(
        r'<div\s+class="[^"]*(?:' + tailwind_pattern + r')[^"]*"[^>]*>',
        '',
        body
    )
    # Remove the corresponding closing </div> tags left orphaned.
    # Strategy: count opening <div> vs closing </div> and remove excess closing tags.
    # First, remove any </div> that appears on a line by itself (whitespace only)
    body = re.sub(r'^\s*</div>\s*$', '', body, flags=re.MULTILINE)

    # Clean up excessive whitespace in tags
    body = re.sub(r'\s+>', '>', body)

    # Collapse multiple spaces within tags to single space
    body = re.sub(r'(<[^>]*?)\s{2,}([^>]*?>)', r'\1 \2', body)

    # Clean up excessive blank lines (3+ newlines -> 2)
    body = re.sub(r'\n{3,}', '\n\n', body)

    return body


def extract_text_preview(body, max_length=200):
    """Extract plain text preview from HTML body for description."""
    if not body:
        return ""
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', body)
    # Decode HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > max_length:
        text = text[:max_length].rsplit(' ', 1)[0] + '...'
    return text


def convert_article(article_path, output_dir):
    """Convert a single article JSON to Hugo markdown."""
    with open(article_path, 'r') as f:
        article = json.load(f)

    article_id = article['id']
    title = article['title']
    body = article.get('body', '')
    created_at = article.get('created_at', '')
    updated_at = article.get('updated_at', '')
    section_id = article.get('section_id', 0)
    original_url = article.get('url', '')
    label_names = article.get('label_names', [])

    section_info = SECTION_MAP.get(section_id, DEFAULT_SECTION)
    section_name = section_info['name']
    category = section_info['category']

    slug = slugify(title)
    body = clean_unicode(body)
    description = extract_text_preview(body)
    cleaned_body = clean_html_body(body)

    # Escape quotes in title for TOML frontmatter
    safe_title = title.replace('"', '\\"')
    safe_description = description.replace('"', '\\"')

    frontmatter = f"""+++
title = "{safe_title}"
date = "{created_at}"
lastmod = "{updated_at}"
slug = "{slug}"
description = "{safe_description}"
original_url = "{original_url}"
article_id = {article_id}
section_id = {section_id}
section_name = "{section_name}"
category = "{category}"
[params]
  section_name = "{section_name}"
  category = "{category}"
  original_url = "{original_url}"
  article_id = {article_id}
+++

"""

    content = frontmatter + cleaned_body + "\n"

    output_path = os.path.join(output_dir, f"{slug}.md")
    with open(output_path, 'w') as f:
        f.write(content)

    print(f"  Created: {slug}.md ({section_name})")
    return slug


def main():
    global VALID_SLUGS

    script_dir = Path(__file__).parent
    clean_articles_dir = script_dir / '..' / 'support' / 'clean_articles'
    output_dir = script_dir / 'content' / 'knowledgebase'

    output_dir.mkdir(parents=True, exist_ok=True)

    json_files = sorted(clean_articles_dir.glob('*.json'))
    print(f"Found {len(json_files)} articles to convert\n")

    # Build the set of valid slugs first (needed for dead link detection)
    for json_file in json_files:
        with open(json_file) as f:
            article = json.load(f)
        VALID_SLUGS.add(slugify(article['title']))

    sections_seen = {}
    for json_file in json_files:
        slug = convert_article(json_file, output_dir)

    print(f"\nDone! Created {len(json_files)} content files in {output_dir}")


if __name__ == '__main__':
    main()
