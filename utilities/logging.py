import logging
from datetime import datetime
import os

# Initialize logger
logger = None

def initialize_logger(log_level=logging.INFO):
    global logger
    if logger:
        return logger

    logger = logging.getLogger("wtz_parser")
    logger.setLevel(log_level)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Use the directory of the calling script instead of the logging script
    calling_script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(calling_script_dir, ".."))
    log_folder = os.path.join(root_dir, "logs")
    
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"wtz_parser_{timestamp}.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Logger initialized")

    return logger
