import tkinter as tk
from tkinter import ttk
import subprocess
import threading
from pathlib import Path
from .monitor import WifiMonitor
from .config import Config
import logging

class ChasingYourTailGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Chasing Your Tail')
        self.config = Config()
        self.monitor = None
        self.setup_ui()
        
    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status section
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="5")
        status_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Stopped")
        self.status_label.grid(row=0, column=0, padx=5)
        
        # Control buttons
        ttk.Button(main_frame, text="Start Monitoring", 
                  command=self.start_monitoring).grid(row=1, column=0, pady=5)
        ttk.Button(main_frame, text="Stop Monitoring", 
                  command=self.stop_monitoring).grid(row=1, column=1, pady=5)
        
        # Configuration section
        config_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="5")
        config_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(config_frame, text="Edit Ignore Lists", 
                  command=self.edit_ignore_lists).grid(row=0, column=0, pady=5)
        ttk.Button(config_frame, text="View Logs", 
                  command=self.view_logs).grid(row=0, column=1, pady=5)
        
    def start_monitoring(self):
        if not self.monitor:
            self.status_label.config(text="Running...")
            self.monitor = WifiMonitor(self.config, None)
            threading.Thread(target=self._run_monitor, daemon=True).start()
        
    def stop_monitoring(self):
        if self.monitor:
            self.monitor.stop()
            self.monitor = None
            self.status_label.config(text="Stopped")
        
    def _run_monitor(self):
        try:
            self.monitor.start()
        except Exception as e:
            logging.error(f"Monitoring error: {e}")
            self.status_label.config(text="Error")
        
    def edit_ignore_lists(self):
        # Implementation for editing ignore lists
        pass
        
    def view_logs(self):
        log_dir = Path(self.config.config['log_dir'])
        if log_dir.exists():
            subprocess.run(['xdg-open', str(log_dir)])

def main():
    root = tk.Tk()
    app = ChasingYourTailGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
