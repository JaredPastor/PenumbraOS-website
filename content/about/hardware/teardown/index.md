+++
title = "Teardown"
description = "Physical teardown documentation of the Ai Pin and Battery Booster."
weight = 20
+++

Internal construction of the Humane Ai Pin and Battery Booster, based on [iFixit's teardown](https://www.ifixit.com/Teardown/Humane+Ai+Pin+Teardown/175765) and FCC internal photo filings ([2BAFM-HU123](https://fccid.io/2BAFM-HU123), [2BAFM-HU223](https://fccid.io/2BAFM-HU223)). For IC-level identification of every chip on the boards, see [Components](../components/).

## Construction

The Ai Pin is a tightly packed device with an internal layout comparable to an Apple Watch in terms of component density. Entry is through adhesive on the back — the rear cover is essentially a wireless charging receiver coil wrapped in plastic.

The main logic board and laser projector board are stacked and connected via flex cables, in a sandwich arrangement similar to modern smartphone PCB designs. A small internal lithium-ion polymer battery is firmly glued in place with no pull tabs.

The Battery Booster is simpler: a battery, wireless charging transmitter coil, and a small control PCB, all held together with adhesive.

## Key Design Details

**Magnetic attachment** — The Pin and Booster connect through clothing via strong magnets. The Booster transmits power wirelessly through fabric to the Pin's STWLC86 receiver.

**Hot-swappable power** — The Pin's internal battery bridges power during Booster swaps. Users can detach a depleted Booster and attach a fresh one without the device shutting down.

**MEMS laser projector** — iFixit identified this as the most innovative hardware component. It uses two STMicroelectronics piezoelectric MEMS mirrors (Castor and Pollux) in a galvo configuration, controlled by a Lattice CrossLink-NX FPGA and a dedicated STM32F412 microcontroller on a separate PCB.

**Compact PCB stacking** — The main board carries the Snapdragon 720G, memory, power management, RF front-end, and sensors. The projector board sits on top with its own FPGA, MCU, laser driver, MEMS mirror driver, and boost converter.

## Repairability

The Ai Pin was designed as a sealed unit and scores poorly on repairability:

- Strong adhesive throughout with no designed entry points
- Battery firmly glued with no pull tabs
- Components soldered directly to the board with no modularity
- No service documentation or replacement parts ever made available by Humane

## FCC Internal Photos

Photos extracted from the FCC equipment authorization filings. These show the PCB layout, component placement, antenna arrangement, and assembly of both devices. Click any thumbnail for the full resolution image.

### Ai Pin Internals

{{< gallery dir="aipin-internals" aspect="wide" >}}

### Battery Booster Internals

{{< gallery dir="booster-internals" aspect="wide" >}}

## References

- [iFixit Teardown: Humane Ai Pin](https://www.ifixit.com/Teardown/Humane+Ai+Pin+Teardown/175765)
- [iFixit Chip ID Guide](https://www.ifixit.com/News/97sp1/humane-ai-pin-chip-id)
- [FCC Filing: Ai Pin (2BAFM-HU123)](https://fccid.io/2BAFM-HU123)
- [FCC Filing: Battery Booster (2BAFM-HU223)](https://fccid.io/2BAFM-HU223)
