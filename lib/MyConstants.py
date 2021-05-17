from cowin_api.constants import Constants


class MyConstants(Constants):
    appointment_by_pin = f"{Constants.base_url}/appointment/sessions/public/findByPin"
    appointment_schedule = f"{Constants.base_url}/appointment/schedule"
    get_otp = f"{Constants.base_url}/auth/generateOTP"
    confirm_otp = f"{Constants.base_url}/auth/confirmOTP"
    beneficiaries = f"{Constants.base_url}/appointment/beneficiaries"
