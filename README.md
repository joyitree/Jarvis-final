# J.A.R.V.I.S

J.A.R.V.I.S - JUST A RATHER VERY INTELLIGENT SYSTEM, inspired by Tony Stark's IRONMAN from the MCU

## DESCRIPTION 🤖
In this project I've created a virtual desktop voice assistant 'JARVIS', which has been creatd by using python as the scripting language. HTML, CSS, jS as the front-end part. And SqLite3 as the database. JARVIS adapts to user needs, providing a seamless and efficient interaction experience.

Currently I've implemented:
```
1. User Login using face recognition
2. Advance GUI using HTML, CSS & jS
3. Provided 25+ features to JARVIS.
```
- Demo video for **JARVIS** is available [here](https://drive.google.com/file/d/1kzvzWTUjsBvG9za_VNQnzm-voxcLa1Kz/view?usp=drive_link)



## Tools & Environment Used

### Hardware Used
- CPU: AMD Ryzen 7 3700X
- RAM: DDR4 8GB * 2
- PCB: Gigabyte X570 Aorus Elite
- GPU: NVIDIA GeForce RTX 2060 Super (vRAM-8GB)
- Full HD webcam with inbuild mic

### Software Used
- OS: Windows 11 Pro(64-bit architecture)
- IDE: Visual Studio Code
- Python 3.12.1


## Features

    1.  Face Recognition for authentication
    2. 	WhatsApp automation
    3.	 Email generation & sending
    4.	 System app opening & closing automation
    5.	 Website opening and closing automation
    6.	 YouTube Search automation
    7.	 Wikipedia search
    8.	 Translation
    9.	 Media playback (using web automation)
    10.	 Weather forecast
    11.	 Trending movies suggestion
    12.	 Current headlines
    13.	 Take note & remember it
    14.	 Take screenshot 
    15.	 LLM model integration
    16.	 Drawing using turtle
    17.	 Internet speed check
    18.	 Computer performance stats
    19.	 Current day & date
    20.	 Current time
    21.  Battery power check
    22.  location detection
    
## Visuals 📸

## UI
Main Hood
![ui3](https://github.com/joyitree/Jarvis-final/assets/93481212/ce3dfa70-f501-4d0e-ad53-cd7113482572)

Listening & Output Display
![ui2](https://github.com/joyitree/Jarvis-final/assets/93481212/72a190fd-aae4-494a-bd4f-ad5a9be18e7e)


Chat History
![ui1](https://github.com/joyitree/Jarvis-final/assets/93481212/131a9f30-b96d-4b6a-bdd3-c3bbcd9f0b90)


## User Authentication

Face Recognition
![face recognition](https://github.com/joyitree/Jarvis-final/assets/93481212/3cfa8923-1066-4ed8-8b19-dbc2b38277da)


Granting Access to Application 
![user verification](https://github.com/bodhisattwaMondal/Jarvis/assets/123143501/cc37d2f8-ef63-4207-9daf-53363f92771e)

## Architecture
![Architecture](https://github.com/bodhisattwaMondal/Jarvis/assets/123143501/1b20eef5-b1c6-45c5-9e3c-6dc05f77ee72)

## Tech Stack
![tech stack](https://github.com/bodhisattwaMondal/Jarvis/assets/123143501/9e07c9aa-3ea8-4599-b564-3caf65b8a3b9)


## Diagrams

Flowchart
![Flowchart](https://github.com/joyitree/Jarvis-final/assets/93481212/6007676e-8efd-4e55-b5ed-622a3a1b0f7b)

DFD
![DFD LEVEL 0](https://github.com/joyitree/Jarvis-final/assets/93481212/70727780-5bfc-4244-ba83-0e6b33218bc2)

![DFD LEVEL 1](https://github.com/joyitree/Jarvis-final/assets/93481212/2843e474-729c-4197-838d-f143234241ff)

![DFD LEVEL 2](https://github.com/joyitree/Jarvis-final/assets/93481212/4da55821-c508-4861-a51f-919473752e8e)


Use Case
![use case diagram](https://github.com/bodhisattwaMondal/Jarvis/assets/123143501/6e8de236-aa03-46b8-be41-714d9444e1f0)

## Project Directory Structure 🌲

```
├── .env
├── .gitignore
├── contacts.csv
├── engine
│   ├── command.py
│   ├── config.py
│   ├── cookies.json
│   ├── db.py
│   ├── features.py
│   └── helper.py
├── jarvis.db
├── main.py
├── requirements.txt
├── run.py
├── run_with_login.py
├── tree.py
├── user_authentication
│   ├── face_recognition.py
│   ├── haarcascade_frontalface_default.xml
│   ├── model trainer.py
│   ├── sample generator.py
│   ├── samples
│   │   └── face.1.1.jpg
│   └── trainer
│       └── trainer.yml
└── www
    ├── assets
    │   ├── audio
    │   │   └── start_sound.mp3
    │   ├── img
    │   │   ├── ironman.ico
    │   │   └── jarvis logo.ico
    │   └── vendore
    │       └── textillate
    │           ├── animate.css
    │           ├── jquery.fittext.js
    │           ├── jquery.lettering.js
    │           └── style.css
    ├── controller.js
    ├── index.html
    ├── main.js
    ├── script.js
    └── style.css

```
## API Keys 🔑

    1. Open Weather: https://openweathermap.org/
    2. NEWS API: https://newsapi.org/
    3. The Movies Database(TMDB) : https://www.themoviedb.org/
    
## Installation 💻

- ### Downloads & Install
    Download & install Python: https://www.python.org/downloads/ 

    Download & install VS Code: https://code.visualstudio.com/download

    Download & install Git bash: https://git-scm.com/downloads
    
    ***NOTE***

    If error appears like : 'git' or 'python' is recognized as an internal/external command, operable program or batch file.

    Add git or python into your system path, environment variable

- ### Clone the project
    First ```fork``` this repository and ```clone``` the repository to your local system 

    ```bash
    $ git clone https://github.com/joyitree/Jarvis.git
    ```
    Now, Open VS Code in the same directory

- ### Create virtual environment 
    I'm naming the env as ```jarvisenv```

    ```bash
    $ python –m venv jarvisenv
    ```
- ### Install dependencies
    Make sure to install all the required python modules mentioned above or you can simply install them by 

    ```bash
    $ pip install -r requirements.txt
    ```

- ### Create enviroment variable
    Create an ```enviroment variable``` .env file in the root directory

    ```
    ASSISTANT_NAME = "Jarvis"
    EMAIL = "None"
    PASSWORD = "None"
    OPENWEATHER_APP_ID = "None"
    NEWS_API_KEY = "None"
    TMDB_API_KEY = "None"
    ```
    NOTE: Replace None with your credentials
- ### Inegrate Hugging Face cookies for login
    ```
    1. Create an account on https://huggingface.co/
    2. Install Cookie-Editor chrome extension in your edge browser
    3. Login in to Hugging Face 
    4. Copy login cookies
    5. Create a cookie.json inside 'engine' folder
    6. Paste login cookies into cookies.json

    ```
- ### Train model for face recognition
    ![face recognition](https://github.com/bodhisattwaMondal/Jarvis/assets/123143501/ff8ee175-7a2f-4a64-a1e2-aa31eb1a15f0)
    ```
    Go to user_authentication folder:
        Create folder: samples & trainer
        Taking Facial Samples-
            - Run sample generator.py 
            - Assign unique ID for each person starting from 1
            - Look at the webcam for face samples 
        
        Training Model-
            - Run model trainer.py
            - It generates trainer.yml under trainer folder 
        
    ```
- ### Create sqlite3 databse (db.py)
    **Import Google Contacts**

    ```
    Go to https://contacts.google.com/
    Export your contacts in Google CSV format
    Paste the file in root directory
    ```

    **Create Database**

    ```bash
    import sqlite2
    import csv

    # Connection
    con - sqlite3.connect("jarvis.db")

    # Cursor
    cursor = con.cursor()
    ```
    **Create Tables**

    ```bash
    # system commands Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command(id integer primary  key, name VARCHAR(100), path VARCHAR(1000)''')


    # web commands Table
    cursor.execute(''''CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000)''')
 

    # contacts Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
    

    # Email Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS email_contacts (id integer primary key, name VARCHAR(200), email VARCHAR(255) NULL)''')
    ```

    **Insert into Tables**
    
    -> System Commands
    
    ```bash
    cursor.execute("INSERT INTO sys_command VALUES (null,'<software name here>', '<software file location here>\\<software name>.exe')")
    
    example: 
    cursor.execute("INSERT INTO sys_command VALUES (null,'calculator', 'C:\\Windows\\System32\\calc.exe')")
    cursor.execute("INSERT INTO sys_command VALUES (null,'msPaint', 'c:\\Windows\\System32\\mspaint.exe')")

    con.commit()  # saving the data on db upto this instance

    ```
    -> Web Commands
    
    ```bash
    cursor.execute("INSERT INTO web_command VALUES (null,'facebook', 'https://www.facebook.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'instagram', 'https://www.instagram.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'flipkart', 'https://www.flipkart.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'amazon', 'https://www.amazon.in/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'netflix', 'https://www.netflix.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'hotstar', 'https://www.hotstar.com/in')")
    cursor.execute("INSERT INTO web_command VALUES (null,'amazon prime', 'https://www.primevideo.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'mail', 'https://mail.google.com/mail/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'maps', 'https://www.google.co.in/maps/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'google news', 'https://news.google.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'google photos', 'https://photos.google.com/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'google calendar', 'https://calendar.google.com/calendar/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'google documents', 'https://docs.google.com/document/')")
    cursor.execute("INSERT INTO web_command VALUES (null,'google spreadsheets', 'https://docs.google.com/spreadsheets/')")
    con.commit()  # saving the data on db upto this instance
    ```
    -> Contacts

    ```bash
    # Specify the column indices you want to import (0-based index)
    # Example: Importing the 1st and 3rd columns
    desired_columns_indices = [0, 32, 30]
    # Read data from CSV and insert into SQLite table for the desired columns
    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            selected_data = [row[i] for i in desired_columns_indices]
            cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no','email') VALUES (null, ?, ?, ?);''', tuple(selected_data))

    #Commit changes and close connection
    con.commit()
    con.close()

    ```

    -> Emails
    ```bash
    # cursor.execute("INSERT INTO email_contacts VALUES (null,'reseiver name','receiver email address')"
    # conn.commit()
    ```

## Future Enhancements ✨

- **Enhanced AI Capabilities**: Implement machine learning models for better understanding and response.

- **Cross-Platform Support**: Extend compatibility to macOS and Linux.

- **Third-Party Integrations**: Integrate with more third-party services like calendars, task managers, and smart home devices.

- **Multilinguial Support**: Support for multiple native languages like Hindi, Bengali, Tamil, etc

- **Android Automation**: Automating tasks on android devices

- **User Customization UI**: User can update his own phonebook, can autorize himself by scannig his face, can set his own commands. Everything right from the JARVIS UI.

