+++
title = "PenumbraOS SDK"
description = "The SDK providing privileged access to apps on the Ai Pin."
weight = 20
+++

## Overview

Placeholder: The PenumbraOS SDK exposes restricted interfaces on the Ai Pin that are normally blocked by the device's SELinux policy.

## Available APIs

Placeholder: Current SDK capabilities:

- **DNS** -- Custom API implementation
- **HTTP** -- Custom API implementation
- **WebSocket** -- Custom API implementation
- **Touchpad** -- Access to touch events and gestures
- **Hand Gestures** -- Gesture recognition
- **Speech Recognition** -- STT access
- **Shell Tunnel** -- Proxied shell commands
- **eSIM Configuration** -- Profile management
- **Settings Management** -- System and app settings with web UI

### Experimental APIs

- Hand Tracking
- Notification (Side) LED

## Architecture

Placeholder: How the SDK bridges the gap between `untrusted_app` and privileged operations using the NFC Binder domain and CVE-2024-31317.

- **Embedded SDK** -- The developer-facing API surface
- **Bridge Service** -- Bridge between SDK and privileged world (runs as `nfc`)
- **Bridge System Service** -- Gateway to privileged operations (runs as `system`)
- **Bridge Settings Service** -- Settings management and embedded web server
- **Bridge Shell Service** -- Shell command proxy

## CLI

Placeholder: The `penumbra` CLI tool at `/data/local/tmp/penumbra` for managing settings and executing actions.

## Source Code

The SDK is open source: [github.com/PenumbraOS/sdk](https://github.com/PenumbraOS/sdk)
