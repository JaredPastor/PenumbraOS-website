+++
title = "Components"
description = "Complete IC component reference for the Ai Pin."
weight = 30
+++

Every identified IC in the Humane Ai Pin, organized by board and side. Identifications sourced from [iFixit's Chip ID guide](https://www.ifixit.com/News/97sp1/humane-ai-pin-chip-id). For internal photos showing component placement, see [Teardown](../teardown/).

## Main Board — Side 1

### Processor & Memory

| Part | Manufacturer | Function |
|------|-------------|----------|
| [SM7125-100-AB](https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-7-series-mobile-platforms/snapdragon-720g-mobile-platform) | Qualcomm | Snapdragon 720G SoC — 8nm, 2x A76 + 6x A55, Adreno 618, Spectra 350L, X15 LTE, 5th Gen AI Engine |
| 32EM32-M4DTX29 | Kingston | 32GB eMMC + 4GB LPDDR4X eMCP |

### Power

| Part | Manufacturer | Function |
|------|-------------|----------|
| [STWLC86](https://www.st.com/en/power-management/stwlc86.html) | STMicroelectronics | Wireless power receiver (Qi-compatible) |
| [MAX77839C](https://www.analog.com/en/products/max77839.html) | Analog Devices | Buck-boost converter |
| [TPS22930A](https://www.ti.com/product/TPS22930A) | Texas Instruments | Load switch (5.5V, 4A, 18mΩ) |

### Security & Control

| Part | Manufacturer | Function |
|------|-------------|----------|
| ST33K | STMicroelectronics | Secure element |
| [CY8C4045FNI-S412T](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-4-32-bit-arm-cortex-m0-mcu/) | Infineon | PSoC 4000S MCU (Cortex-M0) — likely touchpad controller |

### Audio

| Part | Manufacturer | Function |
|------|-------------|----------|
| [WSA8810-0VV](https://www.qualcomm.com/products/technology/analog-semiconductors/audio/wsa8810) | Qualcomm | Mono Class-D speaker amplifier (Aqstic) |

### LED Driver

| Part | Manufacturer | Function |
|------|-------------|----------|
| [LED1202](https://www.st.com/en/power-management/led1202.html) | STMicroelectronics | 12-channel LED driver — drives Trust Light (3 RGB) + Beacon (1 RGB) |

### Sensors

| Part | Manufacturer | Function |
|------|-------------|----------|
| — | STMicroelectronics | 6-axis accelerometer + gyroscope (IMU) |
| [MMC5633NJL](https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MMC5633NJLRevA.pdf) | MEMSIC | 3-axis magnetometer (±30 Gauss, I2C/SPI) |

### RF Front-End

| Part | Manufacturer | Function |
|------|-------------|----------|
| SKYA24000 | Skyworks | Front-end module |
| [SKY77643-61](https://www.skyworksinc.com/) | Skyworks | Multimode multiband PA module |

## Main Board — Side 2

### Power & Charging

| Part | Manufacturer | Function |
|------|-------------|----------|
| PM6250-102 | Qualcomm | Primary PMIC (Snapdragon 720G companion) |
| PM6150A-102 | Qualcomm | Secondary PMIC |
| [BQ25175](https://www.ti.com/product/BQ25175) | Texas Instruments | Linear battery charger (50-500mA) |

### Microcontroller

| Part | Manufacturer | Function |
|------|-------------|----------|
| [STM32F410TB](https://www.st.com/en/microcontrollers-microprocessors/stm32f410tb.html) | STMicroelectronics | Cortex-M4 MCU (100MHz, 128KB Flash) — sensor hub or peripheral management |

### Connectivity

| Part | Manufacturer | Function |
|------|-------------|----------|
| [WCN3988-000](https://www.qualcomm.com/products/technology/wi-fi/wcn3988) | Qualcomm | Wi-Fi 802.11ac (2x2 MIMO) + Bluetooth 5.0 + FM |
| SDR675-005 | Qualcomm | RF transceiver (X15 LTE companion) |
| [SKY53735-61](https://www.skyworksinc.com/) | Skyworks | Diversity receive module (LNA + filter) |
| [SKY13351-378LF](https://www.skyworksinc.com/en/Products/Switches/SKY13351-378LF) | Skyworks | GaAs SPDT RF switch (0.1-6.0GHz) |

## Laser Projector Board — Side 1

The projector has its own dedicated PCB, connected to the main board via flex cable.

### Motor Control & Power

| Part | Manufacturer | Function |
|------|-------------|----------|
| — | STMicroelectronics | MEMS mirror driver (drives Castor + Pollux mirrors) |
| [MP3438GTL](https://www.monolithicpower.com/en/mp3438.html) | Monolithic Power Systems | Boost converter (2.5-22V in, up to 36V out) — MEMS drive voltage |
| [INA280A1QDCKRQ1](https://www.ti.com/product/INA280-Q1) | Texas Instruments | Current sense amplifier (automotive-grade) — laser diode monitoring |

## Laser Projector Board — Side 2

### Digital Control

| Part | Manufacturer | Function |
|------|-------------|----------|
| [LIFCL-17-8UWG72C](https://www.latticesemi.com/Products/FPGAandCPLD/CrossLink-NX) | Lattice Semiconductor | CrossLink-NX FPGA (17K LUTs, 72-ball csBGA) — mirror/laser timing coordination |
| [STM32F412RG](https://www.st.com/en/microcontrollers-microprocessors/stm32f412rg.html) | STMicroelectronics | Cortex-M4 MCU (100MHz, 1MB Flash, 256KB RAM) — projector controller |

### Laser Driver

| Part | Manufacturer | Function |
|------|-------------|----------|
| STLDDx | STMicroelectronics | Laser diode driver — 498nm single-diode, 10ns-20µs variable pulse |

### MEMS Mirrors

| Mirror | Shape | Function |
|--------|-------|----------|
| **Castor** | Circular | Resonant — sweeps horizontal scanlines at fixed frequency |
| **Pollux** | Rectangular | Quasi-static — positions each scanline vertically |

## Architecture

```
┌─────────────────────────────────────────────────┐
│ MAIN BOARD                                      │
│                                                 │
│  Snapdragon 720G ─── Kingston eMCP              │
│  (SoC)               (4GB + 32GB)               │
│    ├── Spectra 350L ISP ── 13MP Camera           │
│    ├── X15 LTE Modem                             │
│    │     ├── SDR675 Transceiver                  │
│    │     ├── SKY77643 PA                         │
│    │     └── SKY53735 / SKY13351 / SKYA24000     │
│    └── AI Engine                                │
│                                                 │
│  WCN3988 (Wi-Fi ac + BT 5.0)                   │
│  PM6250 + PM6150A (PMICs)                       │
│  STWLC86 (Wireless Power Rx) ── Battery         │
│  BQ25175 (Charger)                              │
│  MAX77839C (Buck-Boost)                         │
│  STM32F410TB (Sensor MCU)                       │
│  CY8C4045FNI (Touchpad MCU)                     │
│  ST33K (Secure Element)                         │
│  LED1202 ── Trust Light + Beacon                │
│  WSA8810 ── Speaker                             │
│  IMU + MMC5633NJL + ALS + iToF                  │
│                                                 │
├──────────── flex cable ─────────────────────────┤
│                                                 │
│ PROJECTOR BOARD                                 │
│  LIFCL-17 FPGA ── STM32F412RG MCU              │
│  STLDDx Driver ── 498nm Laser Diode             │
│  ST MEMS Driver ── Castor (H) + Pollux (V)     │
│  MP3438GTL (Boost) + INA280A1 (Current Sense)  │
└─────────────────────────────────────────────────┘
```

## Board Photos

FCC internal photos showing PCB layout and component placement. Click any thumbnail for the full resolution image.

{{< gallery dir="board-photos" aspect="wide" >}}

## References

- [iFixit Chip ID Guide: Humane Ai Pin](https://www.ifixit.com/News/97sp1/humane-ai-pin-chip-id)
- [iFixit Teardown: Humane Ai Pin](https://www.ifixit.com/Teardown/Humane+Ai+Pin+Teardown/175765)
- [FCC Filing: Ai Pin (2BAFM-HU123)](https://fccid.io/2BAFM-HU123)
