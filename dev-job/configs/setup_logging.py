import logging
import logging.config
import os
from pathlib import Path

import coloredlogs
import yaml

from properties import ROOT_DIR

# Create logs folder if it doesn't exist
Path(f"{ROOT_DIR}/logs").mkdir(parents=True, exist_ok=True)

log_config = f"{ROOT_DIR}/configs/logging.yaml"


def setup_logging(default_path=log_config):
    path = default_path
    with open(path, "rt") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def advanced_setup_logging(default_path=log_config, default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print("Error in Logging Configuration. Using default configs")
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print("Failed to load configuration file. Using default configs")
