A WiFi monitoring and analysis tool for Raspberry Pi that helps track and analyze wireless devices in the area.

## Installation

1. Install system requirements:
```bash
sudo apt-get update
sudo apt-get install python3-pip kismet wireless-tools
```

2. Install the package:
```bash
sudo ./install.sh
```

3. Reboot your system:
```bash
sudo reboot
```

## Usage

Start the GUI:
```bash
cyt-gui
```

Or run from command line:
```bash
cyt --monitor-mode
```
