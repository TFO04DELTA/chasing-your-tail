import os
import sys
import logging
import argparse
import time
from pathlib import Path
from .monitor import WifiMonitor
from .database import Database
from .config import Config

def setup_logging(config):
    log_dir = Path(config.config['log_dir'])
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_dir / f"cyt_{time.strftime('%Y%m%d_%H%M%S')}.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    parser = argparse.ArgumentParser(description='Chasing Your Tail - WiFi Monitoring Tool')
    parser.add_argument('--config', type=str, help='Path to config file')
    parser.add_argument('--monitor-mode', action='store_true', help='Set WiFi interfaces to monitor mode')
    args = parser.parse_args()

    # Load configuration
    config = Config(args.config)
    setup_logging(config)
    
    # Initialize components
    db = Database(config)
    monitor = WifiMonitor(config, db)
    
    if args.monitor_mode:
        monitor.enable_monitor_mode()
    
    try:
        monitor.start()
    except KeyboardInterrupt:
        monitor.stop()
        sys.exit(0)
