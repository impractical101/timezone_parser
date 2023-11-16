import json
from urllib.request import urlopen
from utilities.logging import initialize_logger

# Initialize logger
logger = initialize_logger()

def download_time_zones_data(url):
    logger.info(f"Downloading time zones data from URL: {url}")
    try:
        with urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        logger.error(f"Error downloading time zones data: {e}")
        return None

def parse_and_display_time_zones(time_zones, match=None, offset=None):
    logger.info("Parsing downloaded timezones data and displaying it in a user-friendly format.")
    for item in time_zones:
        zone = item.get("value")
        zone_offset = item.get("offset")
        utc_offset = item.get("utc")[0] if item.get("utc") else None
        dst = item.get("isdst", False)

        # Use case-insensitive matching for time zone names
        if (not match or match.lower() in zone.lower()) and (offset is None or offset == zone_offset):
            print(f"Time Zone: {zone}")
            print(f"Offset: {zone_offset}")
            print(f"UTC Offset: {utc_offset}")
            print(f"DST: {'Yes' if dst else 'No'}")
            print("------")

    logger.info("Successfully parsed and displayed the timezones data in the required format")
    if match or offset is not None:
        logger.info("Output filtered based on command-line arguments.")
