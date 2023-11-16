import configparser
from utilities.logging import initialize_logger

logger = initialize_logger()

def read_config(config_file_path):
    logger.info(f"Reading config file from: {config_file_path}")
    config = configparser.ConfigParser()
    config.read(config_file_path)
    logger.info("Config read successfuly")
    return config.get("Settings", "time_zones_url", fallback=None)
