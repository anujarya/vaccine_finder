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

Multiple pin codes with specific vaccine: 
    
    vaccine_finder.exe --pin 201001,250611 --age 45 --dose=2 --vaccine=COVISHIELD

Single pin code with any vaccine:

    vaccine_finder.exe --pin 201001,250611 --age 45 --dose=2 --vaccine=all

Misc Samples :

    vaccine_finder.exe --pin 201001,201002,201019,201009,201002,201012,201014 --age 18 --dose=2 --vaccine=all
    vaccine_finder.exe --pin 201001,201002,201019,201009,201002,201012,201014 --age 18 --dose=1 --vaccine=COVAXIN

## How to test if this app works?

### Test Scenario 1 : Pin code: 250611 and minimum age: 45, dose: 1, app will list all available vaccine slots.

Command :

    vaccine_finder.exe --pin 250611 --age 45 --vaccine all --dose 1

OutPut : 

    Date:24-05-2021, Available Dose 1 Slots:19, Available Dose 2 Slots:5, Center Name: HILWARI, Pin Code:250611, Vaccine: COVISHIELD
    Date:24-05-2021, Available Dose 1 Slots:20, Available Dose 2 Slots:5, Center Name: Chachar Pur, Pin Code:250611, Vaccine: COVISHIELD
    Date:24-05-2021, Available Dose 1 Slots:12, Available Dose 2 Slots:5, Center Name: MALAKPUR, Pin Code:250611, Vaccine: COVISHIELD
    Date:24-05-2021, Available Dose 1 Slots:20, Available Dose 2 Slots:5, Center Name: SABGA SC, Pin Code:250611, Vaccine: COVISHIELD
    Date:24-05-2021, Available Dose 1 Slots:30, Available Dose 2 Slots:5, Center Name: KOTANA, Pin Code:250611, Vaccine: COVISHIELD

### Scenario 2: Pin code: 250611 and minimum age: 18, app will flash no vaccination center available at this pin code.
Command:
    
    vaccine_finder.exe --pin 250611 --age 18 --vaccine all --dose 1

OutPut: 
    
    There is no vaccination center available for pin code:250611

### Provide pin code: 201001 and minimum age: 18, app will run and try to  flash no vaccination center available at this pin code.
Command:
    
    vaccine_finder.exe --pin 201001 --age 18 --vaccine all --dose 1     

OutPut: 

    List of centers with available Vaccine Slots :
    sleeping for 10 seconds.....