+++
title = "MABL Launcher"
description = "The modular assistant and primary user interface for PenumbraOS."
weight = 10
+++

## Overview

Placeholder: MABL is the central orchestrator app for PenumbraOS. It runs as a normal unprivileged app configured as the Android launcher, providing a plugin architecture built around the Android SDK ecosystem.

## Features

Placeholder: Current feature set including:

- Hold one finger to talk to LLM
- Hold two fingers to talk to LLM with a picture
- Conversation persistence
- Laser ink projected display (date/time home screen, conversation display, navigation)
- Dynamic tool calling with cosine similarity matching
- Pluggable tool providers

## Plugin System

Placeholder: How MABL discovers and manages plugins. Plugins register for pre-defined action names and are detected at install/uninstall via `PackageManager`.

## Configuration

Placeholder: How to configure LLM providers, TTS/STT, API keys, and other settings.

## Source Code

MABL is open source: [github.com/PenumbraOS/mabl](https://github.com/PenumbraOS/mabl)
