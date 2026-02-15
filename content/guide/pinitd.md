+++
title = "pinitd"
description = "Custom rootless init system for the Ai Pin."
weight = 30
+++

## Overview

Placeholder: `pinitd` is a custom rootless init system for the Ai Pin that provides persistence (running on boot) and easy developer access to privileged roles. It exposes a similar API surface to `systemd`.

## CLI Commands

Placeholder: The `pinitd-cli` utility provides the following commands:

| Command | Description |
|---------|-------------|
| `start` | Start a service |
| `stop` | Stop a service |
| `restart` | Restart a service |
| `enable` | Enable a service for autostart |
| `disable` | Disable a service |
| `reload` | Reload a service config from disk |
| `reload-all` | Reload all service configs |
| `status` | Show service status |
| `config` | Show service configuration |
| `list` | List all services |
| `shutdown` | Graceful daemon shutdown |

## Service Configuration

Placeholder: Service configuration uses an INI unit file format with `[Service]` and `[Unit]` sections. Key properties include `Name`, `Exec`, `Uid`, `SeInfo`, `Autostart`, and `Restart`.

## Troubleshooting

Placeholder: `pinitd` relies on CVE-2024-31317, which involves a race condition on Android 12+. Failures may cause Zygote to reset. Recovery steps for boot loops.

## Source Code

pinitd is open source: [github.com/PenumbraOS/pinitd](https://github.com/PenumbraOS/pinitd)
