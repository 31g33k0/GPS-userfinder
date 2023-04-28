# GPS-userfinder

## About

This is a simple script to find the location of a user on a map. It uses the osm API to find the location of the user. It uses Leaflet to display the map. The user can use osmand to pass GPS coordinates to the script.

## Installation :

1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt` TODO : add a requirements.txt
3. Run the script using `python3 main.py`

## Usage :

1. Open osmand and go to settings -> General settings -> Share -> Share location -> Share via -> Share with apps -> Select GPS-userfinder`
2. Open the GPS-userfinder app and click on the button to get the location of the user. You can find the web interface of the app at `http://localhost:5000`  (or 0.0.0.0:5000 or 127.0.0.1:5000)
3. The location of the user will be displayed on the map.

## Screenshots :

![Screenshot 1](./assets/screenshot1.png)

## Contents

## TODO's
* screenshots
* diagram
* Rework on the button and make :
    - import a list of users (where, what, will be an user able to register to a private group in the future )
    - create one button for each user
    - onclick center the view on the user and begin to follow (panTO) this user
* Export data button (without suggestion I would pack it in a json data)
* look how to trace an history of positions (is there a inbuilt function or we build the data self. --> the data is small thus a local implementation would spare broadband)

---
optionnal implementings :
* encryption
* Teams
* right levels (admin, team owner, user, other)
* user registration
* Statistics
* API calls parameters (radius, time, etc)
* API calls history (with a map)
* GPS to blockchain (TODO test if it is possible to send a transaction with a GPS position on the ETHBERLIN testnet)

## TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

This repository is under apache 2 licence.  

            Apache License 2.0
            https://www.apache.org/licenses/LICENSE-2.0


## Contributing

Ailox 

## Authors

31g33k0

