+++
title = "Binder Services"
description = "Android Binder IPC services and SELinux restrictions."
weight = 30
+++

## Overview

Placeholder: Detailed documentation of the Binder service landscape on the Ai Pin, SELinux allow/deny rules, and how PenumbraOS works around the restrictions.

## SELinux Policy

Placeholder: Key SELinux rules governing Binder access:

```
(neverallow untrusted_app_all service_manager_type (service_manager (add)))
(neverallow untrusted_app_all protected_service (service_manager (find)))
```

## Available Services

Placeholder: Complete list of Binder services accessible to `untrusted_app` and their capabilities.

## CVE-2024-31317

Placeholder: How the Zygote vulnerability is used to spawn processes in privileged SELinux domains (`nfc`, `radio`, `system`).
