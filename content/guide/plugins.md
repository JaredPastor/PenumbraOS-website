+++
title = "Writing Plugins"
description = "How to build plugins for the MABL launcher."
weight = 40
+++

## Overview

Placeholder: MABL uses a plugin architecture where plugins are separate APKs that register as providers of core features (LLM, TTS, STT, etc.) and can register tool calls for custom functionality.

## Plugin Discovery

Placeholder: Plugins register for pre-defined action names in their `AndroidManifest.xml`:

```xml
<service android:name=".MySttService" android:exported="true">
    <intent-filter>
        <action android:name="com.penumbraos.intent.action.PROVIDE_STT" />
    </intent-filter>
    <meta-data
        android:name="com.penumbraos.metadata.DISPLAY_NAME"
        android:value="My Custom STT" />
</service>
```

## Communication

Placeholder: How plugin logic runs in its own process, binds provider services, and communicates with MABL via the PenumbraOS SDK.

## Rendering UI

Placeholder: How plugins can request UI display within the MABL process. MABL loads plugin UI code via `DexClassLoader`.

## Existing Plugins

Placeholder: List of built-in and community plugins:

- OpenAI-compatible LLM provider
- Humane speech-to-text
- Generic Android TTS
- Google search
- System operations (volume, etc.)
- Ai Pin-specific operations (timers, etc.)
