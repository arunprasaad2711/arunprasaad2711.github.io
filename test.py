import yaml
from pprint import pprint

config_file = "site_config.yaml"

with open(config_file, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

pprint(config["blogfolders"])

