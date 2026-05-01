+++
title = "Getting Started"
description = "Set up PenumbraOS"
weight = 10
icon = "rocket"
+++

{{< callout type="warning" >}}
PenumbraOS is and always will be experimental software. Expect problems and the need to troubleshoot your Pin.
{{< /callout >}}

## Why PenumbraOS

If you want to do anything with the Humane Ai Pin, you don't have any other option. Humane had a strange idea of what "privacy" meant; privacy meant that "no one else can steal your data". That meant that the Ai Pin was locked down tightly, while still sending basically all of your Pin's information to Humane's servers (thus by definition not keeping it private). Even once you've gained access to the Pin using the leaked ADB certificate, apps you install cannot access the network, touchpad, hand gestures, or basically anything else.

After a long and drawn out investigation, PenumbraOS was built to give developers access to the internals of the Ai Pin and to allow them to "fix" the existing Humane cosmOS software; allowing the Ai Pin to largely function as it did before it became defunct.

## What can PenumbraOS do?

In its current iteration, PenumbraOS is designed to function exactly how the Ai Pin did in its prime. The software is all the same, just with tweaks to make it functional.

- Hold a single finger to talk to your Pin
- Double tap two fingers to take a picture
- Double tap and hold two fingers to take a video

PenumbraOS runs a local version of the Humane server that you can access through [Center](/center). Memories such as photos will appear here automatically. You can provide API keys for various LLM providers including OpenAI, Anthropic, Gemini, and custom APIs.

You control everything the Ai Pin does, and can choose how you share your data.

## Requirements

- **Humane Ai Pin**
- **Interposer** - A dock that connects to the Pin's debug interface (four metal pads underneath a sticker on the bottom of the device), which you can connect to a computer using USB. You can [buy one from GoinGhost](https://www.etsy.com/listing/1904242117/ai-pin-usb-dock-slim-final-ver-woptions) or [build your own](https://github.com/PenumbraOS/interposer).
- **Computer with Chrome/Edge** - The installer runs in your browser using WebUSB.
- **LLM API key** - PenumbraOS replaces Humane's cloud services with an LLM you provide. You'll need connection details to an API service; an API URL, API key, and model name. For ease of integrated search and maps, we recommend [Gemini](https://ai.google.dev/gemini-api/docs) (can be used free for some very small number of requests), but [OpenAI](https://platform.openai.com/) is commonly used.

<div class="content-cta">
  <a href="/install/" class="hero-cta">Install PenumbraOS</a>
</div>
