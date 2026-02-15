+++
title = "Development"
description = "Building PenumbraOS from source and contributing."
weight = 50
+++

## Development Setup

Placeholder: How to set up a development environment for PenumbraOS components.

## Building from Source

Placeholder: Each component has a `build.sh` script that sets up the environment on the actual device. Instructions for building MABL, the SDK, and pinitd.

## Project Structure

Placeholder: Overview of the PenumbraOS GitHub organization and how the repositories relate to each other:

- **[mabl](https://github.com/PenumbraOS/mabl)** -- Launcher and user experience (Kotlin)
- **[sdk](https://github.com/PenumbraOS/sdk)** -- Privileged access SDK (Kotlin)
- **[pinitd](https://github.com/PenumbraOS/pinitd)** -- Init system (Rust)
- **[installer](https://github.com/PenumbraOS/installer)** -- Installation tool (Rust/Tauri)
- **[adbd](https://github.com/PenumbraOS/adbd)** -- Custom ADB TCP service
- **[adb_remote_auth](https://github.com/PenumbraOS/adb_remote_auth)** -- Custom ADB client with remote auth (Rust)
- **[interposer](https://github.com/PenumbraOS/interposer)** -- USB access for Ai Pin
- **[app_process-mocks](https://github.com/PenumbraOS/app_process-mocks)** -- Android mock core classes (Kotlin)
- **[3dprints](https://github.com/PenumbraOS/3dprints)** -- 3D models for the Ai Pin

## Contributing

Placeholder: How to contribute to PenumbraOS. Guidelines, issue tracking, pull request process.
