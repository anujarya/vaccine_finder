from lib.MyConstants import MyConstants
from lib.MyCowinApi import MyCoWinAPI
from io import StringIO
import csv
import time
import winsound
import logging
from datetime import datetime

def create_logger():
    logger = logging.getLogger(__name__)
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('vaccine_finder.log')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    return logger


if __name__ == '__main__':
    log = create_logger()
    input_pin_codes = input("Enter pin code: ")
    if input_pin_codes:
        pin_codes = [input_pin_codes]
    else:
        pin_codes = ["201001"]
    min_age_limit = int(input("Minimum age limit(18 or 45): "))
    date = datetime.today().strftime(MyConstants.DD_MM_YYYY)
    cowin = MyCoWinAPI()

    while 1:
        for pin_code in pin_codes.copy():

            if cowin.available_vaccination_center(pin_code, date=date, min_age_limit=min_age_limit) == 0:
                log.info(f"There is no vaccination center available for pin code:{pin_code}\n")
                break

            available_centers = cowin.get_available_slots(pin_code, date, min_age_limit)

            log.info(f"List of centers with available Vaccine Slots :\n")
            for index, center in enumerate(available_centers):
                log.info(
                    f"Date :{center.get('date')}, available_capacity :{center.get('available_capacity')}, pin code :{center.get('pincode')}, Center Name:{center.get('name')}, vaccine : {center.get('vaccine')}\n")
                duration = 100  # milliseconds
                freq = 1840  # Hz
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)

        log.info(f"sleeping for 10 seconds.....")
        time.sleep(10)
