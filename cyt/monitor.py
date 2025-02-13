import subprocess
import time
import sqlite3
from pathlib import Path
import json
import logging

class WifiMonitor:
    def __init__(self, config, database):
        self.config = config
        self.database = database
        self.running = False
        self.ignored_macs = self._load_ignored_macs()
        self.ignored_ssids = self._load_ignored_ssids()
        
    def _load_ignored_macs(self):
        try:
            mac_file = Path(self.config.config['ignore_lists']['mac'])
            if mac_file.exists():
                return set(mac_file.read_text().splitlines())
        except Exception as e:
            logging.error(f"Error loading MAC ignore list: {e}")
        return set()
        
    def _load_ignored_ssids(self):
        try:
            ssid_file = Path(self.config.config['ignore_lists']['ssid'])
            if ssid_file.exists():
                return set(ssid_file.read_text().splitlines())
        except Exception as e:
            logging.error(f"Error loading SSID ignore list: {e}")
        return set()
        
    def enable_monitor_mode(self):
        for interface in self.config.get_interfaces():
            try:
                subprocess.run(['sudo', 'ifconfig', interface, 'down'], check=True)
                subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'monitor'], check=True)
                subprocess.run(['sudo', 'ifconfig', interface, 'up'], check=True)
                logging.info(f"Enabled monitor mode on {interface}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to enable monitor mode on {interface}: {e}")
            
    def start(self):
        self.running = True
        logging.info("Starting WiFi monitoring")
        while self.running:
            try:
                self.scan_networks()
                time.sleep(60)
            except Exception as e:
                logging.error(f"Error during monitoring: {e}")
                time.sleep(5)
    
    def scan_networks(self):
        # Implementation of network scanning logic
        pass
            
    def stop(self):
        self.running = False
        logging.info("Stopping WiFi monitoring")
