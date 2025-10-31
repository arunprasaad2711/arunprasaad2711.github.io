# config_loader.py
from ruamel.yaml import YAML
from pathlib import Path
from typing import Dict, Any

def load_site_config(config_path: str = "site_config.yaml") -> Dict[str, Any]:
    """Load and return site configuration as a dictionary"""
    config_file = Path(config_path)
    
    yaml = YAML()
    # yaml.preserve_quotes = True
    
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.load(f)

# Usage in other scripts
if __name__ == '__main__':
    config = load_site_config()
    print(config['site']['title'])  # "Fluidic Colours"
    print(config['navigation'][0]['label'])  # "Home"