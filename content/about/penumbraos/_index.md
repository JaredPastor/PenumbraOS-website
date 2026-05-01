+++
title = "PenumbraOS"
description = "Jailbreaking Ai Pin."
weight = 10
+++

## system-injector

The current iteration of PenumbraOS is based on CVE-2024-34740 ([PoC](https://github.com/michalbednarski/AbxOverflow)) as implemented in [`system-injector`](https://github.com/PenumbraOS/system-injector). The `system-injector` sets up the vulnerability to install itself as a special app installation method. It's special because it lets you let any app install as `system`, which on the Ai Pin, has nearly full control. In particular, a `system` app is capable of marking itself as `android:process="system"`, which means your process will run inside `system_server`.

`system_server` has very nearly full control of Android, and one of the things it specifically does is controls the launch of every app or Android process on the system. Since we can run inside that process, we can rewrite parts of `system_server` on the fly to do what we want; in our case, hooking into various Humane apps as they start and tweaking them to do our bidding.

## humane-system-hook

Once we're inside and pushing whatever we want into running processes, we bring in [`humane-system-hook`](https://github.com/PenumbraOS/humane-system-hook) to attach to various processes on the system and redirect them. For example:

- Disable telemetry and reporting to Humane domains
- Disable update checking
- Disable periodic crypto signature checks
- Redirect from the real Humane server URL to our own custom one (typically 127.0.0.1)

In the [`humane-system-hook`](https://github.com/PenumbraOS/humane-system-hook) is also a reimplementation of the Humane gRPC server. Using that, we can intercept all of the requests the Pin makes for speech completion, whether, location, etc.
