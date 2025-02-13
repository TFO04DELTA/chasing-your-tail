import sqlite3
from pathlib import Path

class Database:
    def __init__(self, config):
        self.db_path = Path(config.config['database']['path'])
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path / 'cyt.db'))
        self.create_tables()
        
    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS devices (
                    mac TEXT PRIMARY KEY,
                    first_seen INTEGER,
                    last_seen INTEGER,
                    type TEXT
                )
            ''')
            
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS probes (
                    mac TEXT,
                    ssid TEXT,
                    timestamp INTEGER,
                    FOREIGN KEY(mac) REFERENCES devices(mac)
                )
            ''')
