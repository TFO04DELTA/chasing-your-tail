from pathlib import Path
import yaml

class Config:
    def __init__(self, config_path=None):
        self.config_path = Path(config_path) if config_path else Path.home() / '.config' / 'cyt' / 'config.yaml'
        self.config = self._load_config()
        
    def _load_config(self):
        if not self.config_path.exists():
            self._create_default_config()
        return yaml.safe_load(self.config_path.read_text())
    
    def _create_default_config(self):
        default_config = {
            'interfaces': ['wlan0', 'wlan1'],
            'kismet': {
                'log_dir': str(Path.home() / 'kismet_logs'),
                'config_file': '/etc/kismet/kismet_site.conf'
            },
            'database': {
                'path': str(Path.home() / '.local' / 'share' / 'cyt' / 'data'),
            },
            'ignore_lists': {
                'mac': str(Path.home() / '.config' / 'cyt' / 'ignore_mac.txt'),
                'ssid': str(Path.home() / '.config' / 'cyt' / 'ignore_ssid.txt')
            },
            'log_dir': str(Path.home() / '.local' / 'share' / 'cyt' / 'logs')
        }
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(yaml.dump(default_config))
        return default_config

    def get_interfaces(self):
        return self.config['interfaces']
