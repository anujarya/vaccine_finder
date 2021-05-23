# Vaccine Finder for India

## What is this?

This is a console application which let you find available vaccination center in India based on pin code and minimum age (18 or 45).

## How it works?

This application will scan through the Aarogya Setu api and filter the data based on the inputs in an infinite loop with 10 seconds interval.
Once there is a vaccination center meet above criteria and has **Vaccine Slots** available, it will raise alert by making beep sound on your desktop/laptop(make sure you have computer sound on).
The available vaccination center list will be printed on console and in vaccine_finder.log file (created in the same folder as exe).

Once you hear the beeps you need to login to Cowin portal https://selfregistration.cowin.gov.in/ or Aarogya Setu app and book an appointment for one of the slots listed in the console and log file.

## How to use?
### Windows
1. Download the utility from GitHub repo (https://github.com/anujarya/vaccine_finder/blob/main/dist/vaccine_finder.exe )
2. Execute the vaccine finder
3. Input pin code and minimum age (18 or 45)

## Unix/Linux/MacOs
1. Clone the project to local directory.
2. execute the vaccine_finger.py.
3. Input pin code and minimum age (18 or 45)

## Workspace Configuration Instructions
### Python packages
pip install cowin
pip install click
pip install pyinstaller

### Create executable

pyinstaller --onefile vaccine_finder.py

### command line runner without prompts

vaccine_finder.exe --pin 201001 --age 18 --vaccine COVISHIELD --dose 1

vaccine_finder.exe --pin 201001,250611 --age 45 --dose=2 --vaccine=COVISHIELD

vaccine_finder.exe --pin 201001,250611 --age 45 --dose=2 --vaccine=all

## How to test if this app works?

### Test Scenario 1 : Pin code: 250611 and minimum age: 45, app will list all available vaccine slots.

OutPut : 

    Date :17-05-2021, available_capacity :31, pin code :250611, Center Name:KISHANPUR BARAL PHC, vaccine : COVISHIELD

Logs:

    2021-05-17 14:30:11,560 - Starting new HTTPS connection (1): cdn-api.co-vin.in:443
    2021-05-17 14:30:11,833 - https://cdn-api.co-vin.in:443 "GET /api/v2/appointment/sessions/public/calendarByPin?pincode=250611&date=17-05-2021 HTTP/1.1" 200 8134
    2021-05-17 14:30:11,845 - Starting new HTTPS connection (1): cdn-api.co-vin.in:443
    2021-05-17 14:30:11,976 - https://cdn-api.co-vin.in:443 "GET /api/v2/appointment/sessions/public/calendarByPin?pincode=250611&date=17-05-2021 HTTP/1.1" 200 8134
    2021-05-17 14:30:11,982 - Scanning center:{'center_id': 616072, 'name': 'KISHANPUR BARAL PHC', 'address': 'VILL KISHANPUR BARAL', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'fad67d33-deaf-4ac3-979f-44ff9848feca', 'date': '17-05-2021', 'available_capacity': 31, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 21, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,984 - Scanning center:{'center_id': 664195, 'name': 'OSIKKA SC', 'address': 'VILL OSIKKA', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'ac75ee2a-3f70-4812-b3af-e42492654440', 'date': '17-05-2021', 'available_capacity': 50, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 40, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,985 - Scanning center:{'center_id': 562553, 'name': 'UPHC BARAUT PATTI CHAUDHRAN', 'address': 'UPHC PATTI CHAUDHRAN BARAUT', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '74ffdf89-03bf-41f2-8951-c779e64df006', 'date': '17-05-2021', 'available_capacity': 15, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 5, 'available_capacity_dose2': 10}, {'session_id': 'e4f7d2be-472e-4a74-bb46-a5a1861f1ca1', 'date': '18-05-2021', 'available_capacity': 22, 'min_age_limt': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 22}, {'session_id': '4e38c8fb-cbdf-4d51-831d-fd11bc30f33d', 'date': '19-05-2021', 'available_capacity': 24, 'min_age_limt': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 1, 'available_capacity_dose2': 23}, {'session_id': 'a7dc77ef-8331-4dd3-b113-06341b349b1a', 'date': '20-05-2021', 'available_capacity': 24, 'min_age_limt': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 24}, {'session_id': '689da095-0f27-4198-a084-71a0895ae791', 'date': '21-05-2021', 'available_capacity': 40, 'min_age_limt': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'c7c4d8a4-170f-4be7-b0b7-2536f4e196f3', 'date': '22-05-2021', 'available_capacity': 33, 'min_age_limt': 45, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 12, 'available_capacity_dose2': 21}]}
    2021-05-17 14:30:11,985 - Scanning center:{'center_id': 664235, 'name': 'BARWALA SC BARAUT', 'address': 'VILL BARWALA', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 26, 'long': 80, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'b73256ee-3e42-41ac-be41-966c67a72c1e', 'date': '17-05-2021', 'available_capacity': 50, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 40, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,986 - Scanning center:{'center_id': 592547, 'name': 'BIJROL PHC', 'address': 'VILL BIJROL', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '2e54393d-eaa2-424c-8214-3268af655506', 'date': '17-05-2021', 'available_capacity': 42, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 37, 'available_capacity_dose2': 5}]}
    2021-05-17 14:30:11,986 - Scanning center:{'center_id': 664249, 'name': 'BUDHPUR SC', 'address': 'VILL BUDHPUR', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 76, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '7bc64f5e-8e41-477c-b2eb-935367c45a7c', 'date': '17-05-2021', 'available_capacity': 31, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 21, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,986 - Scanning center:{'center_id': 629329, 'name': 'BAWLI PHC', 'address': 'VILL BAWLI', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '1ad9f3d2-2e3e-49fb-ae49-55ecb383d369', 'date': '17-05-2021', 'available_capacity': 41, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 31, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,987 - Scanning center:{'center_id': 592546, 'name': 'GOVT CVC 60 BARAUT CHC', 'address': 'KOTANA ROAD BARAUT', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 26, 'long': 80, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'd6850574-c777-4332-b5c6-1d6b03b4e78b', 'date': '17-05-2021', 'available_capacity': 10, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 5, 'available_capacity_dose2': 5}, {'session_id': 'ae060caa-a54b-47c4-b797-34f24bd17e14', 'date': '18-05-2021', 'available_capacity': 16, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 6, 'available_capacity_dose2': 10}, {'session_id': '32a8144b-1ac5-4240-886c-8e60e8fdcfb9', 'date': '19-05-2021', 'available_capacity': 41, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 32, 'available_capacity_dose2': 10}, {'session_id': 'c581daca-2719-4505-be18-7664f754ab60', 'date': '20-05-2021', 'available_capacity': 43, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 40, 'available_capacity_dose2': 10}, {'session_id': 'fb45a74f-5e14-4bb0-8ae5-90b27317d607', 'date': '21-05-2021', 'available_capacity': 48, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 40, 'available_capacity_dose2': 10}, {'session_id': '83d821d7-dbd2-4f3b-9f66-32dd9d6a6816', 'date': '22-05-2021', 'available_capacity': 39, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 29, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,987 - Scanning center:{'center_id': 664205, 'name': 'LUHARI SC', 'address': 'VILL LUHARI', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'b8fdb88c-b240-4131-b1a0-3b739cf4144c', 'date': '17-05-2021', 'available_capacity': 6, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 6, 'available_capacity_dose2': 0}]}
    2021-05-17 14:30:11,987 - Scanning center:{'center_id': 664242, 'name': 'ANGAD PUR SC', 'address': 'VILL ANGADPUR', 'state_name': 'Uttar Pradesh', 'district_name': 'Baghpat', 'block_name': 'BARAUT', 'pincode': 250611, 'lat': 29, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '950d1c1c-86ef-4ec4-a699-f98e0b1627e4', 'date': '17-05-2021', 'available_capacity': 46, 'min_age_limt': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 36, 'available_capacity_dose2': 10}]}
    2021-05-17 14:30:11,988 - List of centers with available Vaccine Slots :
    2021-05-17 14:30:11,989 - Date :17-05-2021, available_capacity :31, pin code :250611, Center Name:KISHANPUR BARAL PHC, vaccine : COVISHIELD
    2021-05-17 14:30:12,317 - Date :17-05-2021, available_capacity :50, pin code :250611, Center Name:OSIKKA SC, vaccine : COVISHIELD
    2021-05-17 14:30:12,648 - Date :17-05-2021, available_capacity :15, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVISHIELD
    2021-05-17 14:30:12,977 - Date :18-05-2021, available_capacity :22, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVAXIN
    2021-05-17 14:30:13,304 - Date :19-05-2021, available_capacity :24, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVAXIN
    2021-05-17 14:30:13,631 - Date :20-05-2021, available_capacity :24, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVAXIN
    2021-05-17 14:30:13,959 - Date :21-05-2021, available_capacity :40, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVAXIN
    2021-05-17 14:30:14,292 - Date :22-05-2021, available_capacity :33, pin code :250611, Center Name:UPHC BARAUT PATTI CHAUDHRAN, vaccine : COVAXIN
    2021-05-17 14:30:14,625 - Date :17-05-2021, available_capacity :50, pin code :250611, Center Name:BARWALA SC BARAUT, vaccine : COVISHIELD
    2021-05-17 14:30:14,955 - Date :17-05-2021, available_capacity :42, pin code :250611, Center Name:BIJROL PHC, vaccine : COVISHIELD
    2021-05-17 14:30:15,282 - Date :17-05-2021, available_capacity :31, pin code :250611, Center Name:BUDHPUR SC, vaccine : COVISHIELD
    2021-05-17 14:30:15,611 - Date :17-05-2021, available_capacity :41, pin code :250611, Center Name:BAWLI PHC, vaccine : COVISHIELD
    2021-05-17 14:30:15,941 - Date :17-05-2021, available_capacity :10, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:16,267 - Date :18-05-2021, available_capacity :16, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:16,592 - Date :19-05-2021, available_capacity :41, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:16,920 - Date :20-05-2021, available_capacity :43, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:17,250 - Date :21-05-2021, available_capacity :48, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:17,575 - Date :22-05-2021, available_capacity :39, pin code :250611, Center Name:GOVT CVC 60 BARAUT CHC, vaccine : COVISHIELD
    2021-05-17 14:30:17,903 - Date :17-05-2021, available_capacity :6, pin code :250611, Center Name:LUHARI SC, vaccine : COVISHIELD
    2021-05-17 14:30:18,233 - Date :17-05-2021, available_capacity :46, pin code :250611, Center Name:ANGAD PUR SC, vaccine : COVISHIELD
    2021-05-17 14:30:18,560 - sleeping for 10 seconds.....

### Scenario 2: Pin code: 250611 and minimum age: 18, app will flash no vaccination center available at this pin code.
OutPut: 
    There is no vaccination center available for pin code:250611

Logs: 
    2021-05-17 14:33:15,948 - Starting new HTTPS connection (1): cdn-api.co-vin.in:443
    2021-05-17 14:33:16,107 - https://cdn-api.co-vin.in:443 "GET /api/v2/appointment/sessions/public/calendarByPin?pincode=250611&date=17-05-2021 HTTP/1.1" 200 8134
    2021-05-17 14:33:16,109 - There is no vaccination center available for pin code:250611
    
    2021-05-17 14:33:16,110 - sleeping for 10 seconds.....

### Provide pin code: 201001 and minimum age: 18, app will run and try to  flash no vaccination center available at this pin code.
OutPut: 

    List of centers with available Vaccine Slots :
    sleeping for 10 seconds.....

Logs:
 
    2021-05-17 14:33:46,345 - Scanning center:{'center_id': 703134, 'name': 'MMG Kaila Bhatta Covaxin 18-44', 'address': 'Kaila Bhatta Village Madhopura Ghaziabad', 'state_name': 'Uttar Pradesh', 'district_name': 'Ghaziabad', 'block_name': 'Kaila Bhatta', 'pincode': 201001, 'lat': 28, 'long': 77, 'from': '09:00:00', 'to': '17:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '3aecd25d-1213-452c-b056-d0be8a1d7153', 'date': '17-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '4b61b458-91f9-4444-90a1-14721b500158', 'date': '18-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVAXIN', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '35a16429-a659-4dde-8da3-466c583dca9e', 'date': '19-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVAXIN', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}]}
    
    2021-05-17 14:33:46,345 - Scanning center:{'center_id': 702429, 'name': 'UPHC BLS 18 To 44', 'address': 'Bls Inds Area Yadav Ngr Near Rto Office Ghaziabad', 'state_name': 'Uttar Pradesh', 'district_name': 'Ghaziabad', 'block_name': 'Bulandsahar Industrial Area', 'pincode': 201001, 'lat': 28, 'long': 77, 'from': '10:00:00', 'to': '16:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '0cc11609-53bd-481b-b1fa-983fb249caef', 'date': '17-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'eee5729e-b5b5-44e2-8641-5b65d1d260e0', 'date': '18-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '5cf800e6-0d6e-4c43-846c-df91fea32876', 'date': '19-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '9cd2516f-443a-472f-8e32-0f54a8f9acfa', 'date': '20-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'c7d951eb-5654-47b0-980a-e93d4bc68673', 'date': '21-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '133f75b6-0d3d-4a44-a67a-204f137ff133', 'date': '22-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}]}
    
    2021-05-17 14:33:46,345 - Scanning center:{'center_id': 563863, 'name': 'DWH 18 To 44', 'address': 'G.T ROAD JASSI PURA GHAZIABAD', 'state_name': 'Uttar Pradesh', 'district_name': 'Ghaziabad', 'block_name': 'District Women Hospital (PPC)', 'pincode': 201001, 'lat': 28, 'long': 77, 'from': '10:00:00', 'to': '16:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': '2e64f005-b81b-486b-9a57-edc9bd39fb8c', 'date': '17-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '7a6c2639-3bea-4ff8-8e35-4526f38d7816', 'date': '18-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'f598d975-5c0c-4e60-8bf1-7b8ff9d3492f', 'date': '19-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'ec3d68be-cbfe-438a-8eb1-c7cda9ce09ee', 'date': '20-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '1c182211-308f-4272-8a54-2324f7340c6f', 'date': '21-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'e13a9506-6ac2-40e1-9eba-bc1cfd39a73b', 'date': '22-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}]}
    
    2021-05-17 14:33:46,345 - Scanning center:{'center_id': 697544, 'name': 'UPHC Carte 18 To 44', 'address': 'Uphc Shastri Nagar Mahendra Enclave Near By Silver Shine School Ghaziababd', 'state_name': 'Uttar Pradesh', 'district_name': 'Ghaziabad', 'block_name': 'Carte(Shastrinagar)', 'pincode': 201001, 'lat': 28, 'long': 77, 'from': '10:00:00', 'to': '16:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'ec3621b0-3597-4d76-b4ae-5c9d9e856f90', 'date': '17-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '46799472-1342-4944-97ef-31d6cc2cd584', 'date': '18-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'b65c453d-132f-4cad-99ee-4968a4a8f24b', 'date': '19-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'b196aba1-e445-4270-a5f6-5d90d362fa30', 'date': '20-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': 'd646e5bf-3874-418d-bc4d-cc09db4cff13', 'date': '21-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}, {'session_id': '50da17d6-384e-4bf7-ade0-fc370919f0d0', 'date': '22-05-2021', 'available_capacity': 0, 'min_age_limt': 18, 'vaccine': 'COVISHIELD', 'slots': ['10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-01:00PM', '01:00PM-04:00PM'], 'available_capacity_dose1': 0, 'available_capacity_dose2': 0}]}
    
    2021-05-17 14:33:46,345 - List of centers with available Vaccine Slots :
    
    2021-05-17 14:33:46,345 - sleeping for 10 seconds.....
