import argparse
import os
from utilities.config import read_config
from utilities.timezones import download_time_zones_data, parse_and_display_time_zones
from utilities.logging import initialize_logger

# Initialize logger
logger = initialize_logger()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Display information about world time zones.")
    parser.add_argument("--match", help="Display only information about time zones whose values match the specified string.")
    parser.add_argument("--offset", type=int, help="Display time zones matching this offset.")
    args = parser.parse_args()

    # Log command-line arguments
    logger.info(f"Command-line arguments: --match={args.match}, --offset={args.offset}")

    return args

def main():
    logger.info("**** STARTING THE TIMEZONE PARSER APPLICATION ****")

    # Parse command-line arguments
    args = parse_arguments()

    # Read URL from config file
    config_file_path = os.path.join(os.path.dirname(__file__), "config", "wtz_parser.ini")
    time_zones_url = read_config(config_file_path)

    if not time_zones_url:
        logger.error("Invalid or missing time_zones_url in the config file.")
        return

    # Download time zones data
    time_zones_data = download_time_zones_data(time_zones_url)

    if time_zones_data is not None:
        # Parse and display time zones based on command-line arguments if provided
        logger.info("Timezones data download successful")
        parse_and_display_time_zones(time_zones_data, match=args.match, offset=args.offset)

    logger.info("**** TIMEZONE PARSER APPLICATION ENDED  ****")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
