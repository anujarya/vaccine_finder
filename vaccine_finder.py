from lib.MyConstants import MyConstants
from lib.MyCowinApi import MyCoWinAPI
import time
import winsound
import logging
from datetime import datetime
import click


def create_logger():
    logger = logging.getLogger(__name__)
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('vaccine_finder.log')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(message)s')
    f_format = logging.Formatter('%(asctime)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    return logger


@click.command()
@click.option('--pin', prompt='Pin Code(CSV)', default="201001", help='Specify the pin code you want to search for.')
@click.option('--age', prompt='Age(18, 45, both)', default="18", help='Minimum age to find the vaccine.')
@click.option('--dose', prompt='Dose Number(1 or 2, default is 1)', default=1, help='Dose number you are looking for.',
              required=True)
@click.option('--vaccine', prompt='Vaccine Name(default is all)', default="all",
              help='Name of the vaccine you are looking for.')
def main(pin, age, vaccine, dose):
    log = create_logger()
    pin_codes = pin.split(',')

    if vaccine == "all":
        vaccine = None
    if age == "both":
        min_age_limit = None
    else:
        min_age_limit = int(age)

    date = datetime.today().strftime(MyConstants.DD_MM_YYYY)
    cowin = MyCoWinAPI()

    slot_filters = {
        "min_age_limit": min_age_limit,
        "vaccine": vaccine,
    }

    dose_key = "available_capacity_dose1" if dose == 1 else "available_capacity_dose2"

    while 1:
        for pin_code in pin_codes.copy():
            if cowin.available_vaccination_center_by_age(pin_code, date, {"min_age_limit": min_age_limit}) == 0:
                log.info(f"There is no vaccination center available for pin code:{pin_code}\n")
                break

            available_centers = cowin.get_available_slots(pin_code, date, dose_key, slot_filters)

            log.info(f"List of centers with available Vaccine Slots for pin code:{pin_code}:\n")
            for index, center in enumerate(available_centers):
                log.info(
                    f"Date:{center.get('date')}, Available Dose 1 Slots:{center.get('available_capacity_dose1')}, "
                    f"Available Dose 2 Slots:{center.get('available_capacity_dose2')}, Center Name: {center.get('name')}, "
                    f"Pin Code:{center.get('pincode')}, Vaccine: {center.get('vaccine')}")
                duration = 100  # milliseconds
                freq = 1840  # Hz
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)
                winsound.Beep(freq, duration)

        log.info(f"sleeping for 10 seconds.....")
        time.sleep(10)


if __name__ == '__main__':
    main()
