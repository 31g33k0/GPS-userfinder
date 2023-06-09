# GPS-userfinder

## About

This is a simple script to find the location of a user on a map. It uses the osm API to find the location of the user. It uses Leaflet to display the map. The user can use osmand to pass GPS coordinates to the script.

## Installation :

1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt` TODO : add a requirements.txt
3. Run the script using `python3 main.py`

## Usage :

1. On your smartphone (android), get Osmand from F-droid (the google play store version has not the needed feature to pipe GPS coordinates to a custom URL)
2. Open the options panel, extensions (erweiterungen in German version), add Path descriptions (Streckenaufzeichnung). go back on the map GUI and notice the REC button. push it (go in Options to fine grain your demand). you can now start and pause the tracking. Do not forget to give autorizations to Osmand to access the GPS. Optionnally wou can updates coordinates manually, see the point 4
3. Start the script by typing `python3 main.py` or equivalent from the application folder. Note that it may not work with pyhton 2.7 or older.
4. Open the GPS-userfinder web-app and click on the button to get the location of the user. You can find the web interface of the app at `http://localhost:5000`  (or 0.0.0.0:5000 or 127.0.0.1:5000).   
If you are experiencing issues with Osmand, or want to give the coordinates from another source, you can update coordinates "manually" here :   
`http://localhost:5000/update?lat=0&lon=0`   
change the 0 by the lat and lon values respectively
5. Done ! The location of the user will be displayed on the map.

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
* https would be mandatory if credentials are added from a precedent feature.

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

