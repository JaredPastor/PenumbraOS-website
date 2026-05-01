+++
title = "Overview & Specs"
description = "Hardware specifications and form factor of the Humane Ai Pin."
weight = 10
+++

The Humane Ai Pin is a screenless, standalone wearable device designed by ex-Apple engineers and manufactured by Compal Electronics. It launched April 11, 2024 at $699-$799 with a required $24/month T-Mobile plan. The Charge Case accessory was [recalled in June 2024](https://www.cpsc.gov/Recalls/2024/Humane-Recalls-Charge-Case-for-Ai-Pin-Due-to-Fire-Hazard) due to a fire hazard; the recall does not affect the Pin or Battery Booster. Humane was later acquired by HP Inc.

## Key Specs

| | |
|---|---|
| **Processor** | [Qualcomm Snapdragon 720G](https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-7-series-mobile-platforms/snapdragon-720g-mobile-platform) — 2x Cortex-A76 @ 2.3GHz + 6x Cortex-A55 @ 1.8GHz, 8nm |
| **GPU** | Adreno 618 |
| **RAM** | 4GB LPDDR4X |
| **Storage** | 32GB eMMC |
| **Display** | Laser Ink Display — 720p MEMS laser projector, 498nm green, Class 2 |
| **Camera** | 13MP ultrawide, 120° FOV, f/2.4, 1080p 30fps video |
| **Depth Sensor** | iToF, 640x480, 125° FOV |
| **Cellular** | LTE (13 FDD + 2 TDD bands), UMTS/HSPA+, eSIM (T-Mobile) |
| **Wi-Fi** | 802.11ac (Wi-Fi 5), 2.4GHz + 5GHz |
| **Bluetooth** | 5.1 — SBC, AAC, LDAC, aptX HD |
| **Positioning** | GPS, GLONASS, Galileo, BeiDou, A-GPS, Wi-Fi |
| **OS** | Android 12 (system), Android 11 (vendor), Linux 4.14.190 kernel |
| **Weight** | 34.2g (Pin) + 20.5g (Booster) = ~55g on body |
| **Dimensions** | 47.5 x 44.5 x 15mm (Pin), 47.2 x 45.2 x 8.3mm (Booster) |

## Processor

The Snapdragon 720G (SM7125-100-AB, codename "Atoll AB") is a mid-range mobile SoC on Samsung's 8nm LPP process. It integrates the Snapdragon X15 LTE modem, Spectra 350L image signal processor, Adreno 618 GPU, and 5th Gen Qualcomm AI Engine. RAM and storage are provided by a single Kingston 32EM32-M4DTX29 eMCP package combining 4GB LPDDR4X and 32GB eMMC.

## Laser Ink Display

The primary display is a MEMS-based laser projector that projects a green monochrome image onto the user's palm. It uses two STMicroelectronics piezoelectric MEMS mirrors in a galvo configuration:

- **Castor** (circular) — Resonant mirror sweeping horizontal scanlines
- **Pollux** (rectangular) — Quasi-static mirror positioning each scanline vertically

A Lattice CrossLink-NX FPGA coordinates mirror timing with the laser modulation. The projector has its own dedicated PCB with a separate STM32F412 microcontroller. See [Components](../components/) for the full projector board IC listing.

| | |
|---|---|
| **Resolution** | 720p |
| **Laser** | Custom single-diode, 498nm peak, 25mW peak, Class 2 (IEC 60825-1:2014) |
| **Pulse Duration** | 10ns - 20µs (variable) |
| **Operating Distance** | 20-40cm |
| **FOV** | 18.2° x 13.3° (22.4° diagonal) — ~7 x 9.6cm at 30cm |

## Camera & Depth Sensor

| | Camera | Depth Sensor |
|---|---|---|
| **Type** | RGB | Indirect Time-of-Flight (iToF) |
| **Resolution** | 13MP | 640 x 480 (VGA) |
| **FOV** | 120° (ultrawide) | 125° |
| **Aperture** | f/2.4 | f/1.4 |
| **Lens** | 5-element (1 glass) | 4-element |
| **Focal Distance** | 40cm - infinity | — |
| **Video** | 1080p @ 30fps | — |

## Connectivity

**Cellular:** Dual antenna MIMO LTE via the integrated Snapdragon X15 modem. FDD-LTE bands 1/2/3/4/5/7/8/12/17/20/26/66/71, TDD-LTE bands 38/41, UMTS/HSPA+/DC-HSDPA fallback. eSIM on the T-Mobile network. VoLTE and 3G voice calling supported.

**Wi-Fi:** 802.11a/b/g/n/ac (Wi-Fi 5) on 2.4GHz and 5GHz via Qualcomm WCN3988.

**Bluetooth:** 5.1 with SBC, AAC, LDAC, and aptX HD codec support.

**Positioning:** GPS, GLONASS, Galileo, BeiDou, A-GPS, and Wi-Fi positioning.

## Sensors & Indicators

| Sensor | IC |
|--------|-----|
| Accelerometer + Gyroscope | STMicroelectronics (6-axis IMU) |
| Magnetometer | [MEMSIC MMC5633NJL](https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MMC5633NJLRevA.pdf) (3-axis) |
| Ambient Light Sensor | Integrated |

**Trust Light:** 3 RGB LEDs on the front face indicating camera/microphone activity. Driven by an [STMicroelectronics LED1202](https://www.st.com/en/power-management/led1202.html) 12-channel driver.

**Beacon:** 1 RGB LED for status/notification, also driven by the LED1202.

## Form Factor

The system consists of two magnetically coupled halves that sandwich the user's clothing:

- **Ai Pin** (outward) — All compute, sensors, and projector. 47.5 x 44.5 x 15mm, 34.2g.
- **Battery Booster** (inward) — Battery + wireless charging transmitter. 47.2 x 45.2 x 8.3mm, 20.5g. Hot-swappable without powering down (the Pin's internal battery bridges the gap).

The front face has the camera, depth sensor, projector aperture, Trust Light, and a capacitive touchpad for gesture input. An [STMicroelectronics STWLC86](https://www.st.com/en/power-management/stwlc86.html) wireless power receiver in the Pin receives power from the Booster through fabric.

### Colors

| Color | Finish | Price |
|-------|--------|-------|
| Eclipse | Matte black | $699 |
| Equinox | Polished silver, black touchpad | $799 |
| Lunar | Polished silver, white touchpad | $799 |

### FCC Label

The Ai Pin uses an electronic label (e-label) displayed via the laser projector rather than a physical label. FCC IDs: [2BAFM-HU123](https://fccid.io/2BAFM-HU123) (Pin), [2BAFM-HU223](https://fccid.io/2BAFM-HU223) (Booster).

### Charging

- **Charge Pad** — Desk charger for Pin + Booster. Has a pinhole reset button on the underside.
- **Charge Case** — Portable case holding the Pin and two Boosters. Charges via USB-C. Recalled June 2024 due to battery fire hazard.

### Environmental Limits

Operating temperature 5-35°C. Maximum altitude 3,000m.

## FCC Photos

Photos from the FCC equipment authorization filings. Click any thumbnail for the full resolution image.

### Ai Pin Exterior

{{< gallery dir="aipin-exterior" aspect="wide" >}}

### Battery Booster Exterior

{{< gallery dir="booster-exterior" aspect="wide" >}}
