#!/usr/bin/env bash
set -euo pipefail

hugo
npx pagefind --site public
