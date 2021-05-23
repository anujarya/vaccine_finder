from lib.MyConstants import MyConstants
import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError
import logging

from typing import Union, List

from cowin_api.base_api import BaseApi
from cowin_api.utils import today


class MyCoWinAPI(BaseApi):
    logging.basicConfig(filename='vaccine_finder.log', filemode='w', format='%(asctime)s - %(message)s',
                        level=logging.DEBUG)

    def get_states(self):
        url = MyConstants.states_list_url
        return self._call_api(url)

    def get_districts(self, state_id: str):
        url = f"{MyConstants.districts_list_url}/{state_id}"
        return self._call_api(url)

    def filter_centers(self, centers: dict, filters: dict):
        original_centers = centers.get('centers')
        filtered_centers = {'centers': []}
        for index, center in enumerate(original_centers):
            filtered_sessions = []
            for session in center.get('sessions'):
                matched = True
                for key in filters.keys():
                    matched = matched and ((not filters.get(key)) or session.get(key) == filters.get(key))
                if matched:
                    filtered_sessions.append(session)
            if len(filtered_sessions) > 0:
                center['sessions'] = filtered_sessions
                filtered_centers['centers'].append(center)
        return filtered_centers

    def get_availability_by_base(self, caller: str, areas: Union[str, List[str]], date: str, filters: dict):
        """this function is called by the get availability function
        this is separated out so that the parent functions have the same
        structure and development becomes easier"""
        area_type, base_url = 'pincode', MyConstants.availability_by_pin_code_url
        if caller == 'district':
            area_type, base_url = 'district_id', MyConstants.availability_by_district_url
        # if the areas is a str, convert to list
        if isinstance(areas, str):
            areas = [areas]
        # make a separate call for each of the areas
        results = []
        for area_id in areas:
            url = f"{base_url}?{area_type}={area_id}&date={date}"
            if filters:
                curr_result = self.filter_centers(self._call_api(url), filters)
            else:
                curr_result = self._call_api(url)
            # append
            if curr_result:
                results += curr_result['centers']

        # return the results in the same format as returned by the api
        return {'centers': results}

    def get_availability_by_pincode(self, pin_code: Union[str, List[str]],
                                    date: str = today(),
                                    filters: dict = {}):
        return self.get_availability_by_base(caller='pincode', areas=pin_code,
                                             date=date, filters=filters)

    def post_api(self, url, data) -> Union[HTTPError, dict]:
        user_agent = UserAgent()
        headers = {'User-Agent': user_agent.random}
        response = requests.post(url, data=data, headers=headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e

        return response.json()

    def get_available_slots(self, pin_code, date, dose_key, filters: dict):
        available_centers = self.get_availability_by_pincode(pin_code, date, filters)
        filtered_centers = []
        for index, center in enumerate(available_centers.get("centers")):
            logging.info(f"Scanning center:{center}\n")
            for session in center.get("sessions"):
                if session.get(dose_key) > 0:
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
                        "available_capacity_dose1": session.get("available_capacity_dose1"),
                        "available_capacity_dose2": session.get("available_capacity_dose2"),
                        "min_age_limt": session.get("min_age_limt"),
                        "vaccine": session.get("vaccine")
                    })
        return filtered_centers

    def available_vaccination_center_by_age(self, pin_code, date, filters: dict) -> int:

        available_centers = self.get_availability_by_pincode(pin_code, date, filters)
        return len(available_centers.get("centers"))
