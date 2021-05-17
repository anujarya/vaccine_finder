from cowin_api.api import CoWinAPI

from lib.MyConstants import MyConstants
from typing import Union

import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError
import logging


class MyCoWinAPI(CoWinAPI):
    logging.basicConfig(filename='vaccine_finder.log', filemode='w', format='%(asctime)s - %(message)s',
                        level=logging.DEBUG)

    def post_api(self, url, data) -> Union[HTTPError, dict]:
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.random}
        response = requests.post(url, data=data, headers=headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e

        return response.json()

    def get_available_slots(self, pin_code, date, min_age_limit):
        available_centers = CoWinAPI.get_availability_by_pincode(self, pin_code, date, min_age_limit)
        filtered_centers = []
        for index, center in enumerate(available_centers.get("centers")):
            logging.info(f"Scanning center:{center}\n")
            for session in center.get("sessions"):
                if session.get("available_capacity") > 0:
                    filtered_centers.append({
                        "center_id": center.get("center_id"),
                        "name": center.get("name"),
                        "address": center.get("address"),
                        "district_name": center.get("district_name"),
                        "pincode": center.get("pincode"),
                        "fee_type": center.get("fee_type"),
                        "session_id": session.get("session_id"),
                        "date": session.get("date"),
                        "available_capacity": session.get("available_capacity"),
                        "min_age_limit": session.get("min_age_limit"),
                        "vaccine": session.get("vaccine")
                    })
        return filtered_centers

    def available_vaccination_center(self, pin_code, date, min_age_limit) -> int:
        available_centers = CoWinAPI.get_availability_by_pincode(self, pin_code, date, min_age_limit)
        return len(available_centers.get("centers"))
