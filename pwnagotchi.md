# Pwnagotchi: Wi-Fi Sniffing AI Companion
**Pwnagotchi** is an open-source tool that passively collects Wi-Fi handshakes to help with WPA/WPA2 network auditing.

This page documents my setup, experiments, and learnings with Pwnagotchi for educational cybersecurity purposes.

## SETUP

Hardware:
- Raspberry Pi Zero 2 W
- Waveshare E-Paper HAT+
- 32gb microSD

Software:
- [jayofelony Pwnagotchi image](https://github.com/jayofelony/pwnagotchi)
The original Pwnagotchi project is no longer actively maintained, so I'm using a community-updated fork by Jayofelony. This version is optimized for the Raspberry Pi Zero 2 W by removing the AI component, which improves stability, increases uptime, and extends battery life.
- [Project Pwnag0dchi](https://github.com/SHUR1K-N/Project-Pwnag0dchi)
Modifying with Pwnag0dchi for extra features for network testing.
- [RPi imager](https://www.raspberrypi.com/software/)
- [FileZilla](https://filezilla-project.org/)
  
## Learnings
- Pwnagotchi wasn't booting properly, tried different images to no avail but realized something in the config.toml was messing up the booting process.
- Was able to boot in auto mode but device wouldn't be found in network connections even with RSIND driver installed, BUT working as usual.
- After replugging the USB the Pi would boot but the display would switch and freeze and the device would become unresponsive.
- Trying to understand why Pi wouldn't work when connecting to PC via data port. Either my PC would bluescreen or the Pi would become unresponsive.
- Figured out that my motherboard couldn't handle the load, so I connected the Pi to a portable power bank, then connected to PC via data port, then the PC was able to detect the Pi as a RNDIS device.
- Able to assign static IP to the device and was able to SSH in.

## Experiments
- Trying to add Pwnag0dchi plugins.
- Customized UI

