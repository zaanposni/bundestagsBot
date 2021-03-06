import os.path

from . import handleJson
from .console import Console, red, white

BASE_PATH = content_dir = "config" if os.path.isdir("config") else "config-default"

PATHS = ["blacklist.json", "main.json", "messages.json",
         "role_table.json", "tokens.json", "analyzer.json"]
SHL = Console("ConfigLoader", cls=True)


class Config:
    def __init__(self):
        self.options = {}
        self.reload()

    def reload(self, debug=False):
        SHL.output(f"Reloading config.")
        files_failed = 0
        for path in PATHS:
            SHL.output(f"Reloading configfile {os.path.join(BASE_PATH, path)}")
            data = handleJson.readjson(os.path.join(BASE_PATH, path))
            if data is None:
                files_failed += 1
                continue
            for key, value in data.items():
                self.options[key] = value
                if debug:
                    SHL.output(f"[{key}]: {value}")
        SHL.output(f"{red}========================{white}")
        return files_failed

    def get(self, key: str, default=None):
        return self.options.get(key, default)


cfg = Config()
