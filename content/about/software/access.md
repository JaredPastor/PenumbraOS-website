+++
title = "Access & Security"
description = "ADB access, security model, and device restrictions."
weight = 20
+++

## ADB Access

Placeholder: The primary access mechanism is ADB with the leaked Humane ADB certificate. This is likely the only infiltration method available.

## Blocked Communication

Placeholder: Communication methods blocked by SELinux:

- Direct network access
- DNS
- Sockets
- Unix domain sockets (almost works but no app-to-shell communication)
- Named pipes

File-based communication between processes is possible. The `shell` user has networking permission and can act as a bridge.

## Binder Services

Placeholder: Binder access is restricted by SELinux policy. Available services for `untrusted_app`:

- `audioserver_service`
- `cameraserver_service`
- `drmserver_service`
- `mediaserver_service` / `mediaextractor_service` / `mediametrics_service` / `mediadrmserver_service`
- `nfc_service`
- `radio_service`
- `app_api_service`
- `vr_manager_service`

The `nfc` and `radio` domains are accessible via CVE-2024-31317, which is the communication method used by the PenumbraOS SDK.

## Other Restrictions

Placeholder:

- Touchpad access blocked from userland (data can be intercepted by `shell` user)
- Services cannot be started directly using `startService` from `untrusted_app`
- No `untrusted_app` to `system_app` communication
