# install.sh:
#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root"
    exit 1
fi

# Install system dependencies
apt-get update
apt-get install -y python3-pip kismet wireless-tools

# Install Python package
pip3 install .

# Setup Kismet
usermod -aG kismet $SUDO_USER

# Create necessary directories
mkdir -p /etc/kismet
cat > /etc/kismet/kismet_site.conf << EOF
source=wlan0
source=wlan1
log_prefix=/home/pi/kismet_logs/
EOF

# Create autostart entry
mkdir -p /etc/xdg/autostart
cat > /etc/xdg/autostart/cyt-gui.desktop << EOF
[Desktop Entry]
Name=Chasing Your Tail
Exec=cyt-gui
Type=Application
EOF

echo "Installation complete! Please reboot your system."
