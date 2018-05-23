# Xbee Configuration:

* xBee PAN_ID is set to 2222 for all modules
* Winch side xBee must be configured as Coordinator, with API mode enabled (no escaping - mode 1)
* Plane side xBees are either routers or endpoints, with API mode enabled (with escaping - mode 2). DH and DL must either be 0 or set to the Coordinator addresses

# Python dependencyes:

* Python3
* kivy
* kivyMD
* python-xBee (https://github.com/niolabs/python-xbee)
* matplotlib
* kivy-garden.matplotlib
