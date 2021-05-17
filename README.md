# Vaccine Finder

This is a console application which let you find available vaccination center in India based on pin code and minimum age (18 or 45).

## How to use
### Windows
1. Download the utility from GitHub repo 
2. Execute the vaccine finder
3. Input pin code and minimum age (18 or 45)

## Unix/Linux/MacOs
1. Clone the project to local directory.
2. execute the vaccine_finger.py.
3. Input pin code and minimum age (18 or 45)

## How it works?

This application will scan through the Aarogya Setu api and filter the data based on the inputs.
Once there is a vaccination center meet above criteria and has **Vaccine Slots** available, it will raise alert by making beep sound on your desktop/laptop(make sure you have computer sound on).
The available vaccination center list will be printed on console and in vaccine_finder.log file (created in the same folder as exe).

Once you hear the beeps you need to login to Cowin portal https://selfregistration.cowin.gov.in/ or Aarogya Setu app and book an appointment for one of the slots listed in the console and log file.

