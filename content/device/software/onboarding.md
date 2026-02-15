+++
title = "Onboarding & Provisioning"
description = "Factory reset state, provisioning process, and cleanup."
weight = 40
+++

## Factory Reset State

Placeholder: After a factory reset, the Ai Pin enters an onboarding state that requires Humane's servers (which are now offline) to complete provisioning.

## Provisioning Investigation

Placeholder: Findings from investigating the provisioning process:

- Provisioning requires multi-step network calls to Humane servers
- All network calls use an embedded cert in the APK
- The cert can be bypassed in specific conditions but the endpoint no longer exists
- `humaneinternal.system.ProvisioningService` is bindable but still requires network access
- Cannot directly write fake credentials into `AndroidKeyStore`

## Workaround

Placeholder: How to get a factory-reset device into a usable state:

- Disabling onboarding (`pm disable-user --user 0 humane.experience.onboarding`) starts the normal launcher
- Must also disable `ironman` (`pm disable-user --user 0 hu.ma.ne.ironman`) to stop service crash loops

## Resetting

Placeholder: How to reset the Ai Pin using the Charge Pad reset button (paperclip method).
