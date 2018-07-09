# Xbee Configuration:

* xBee PAN_ID is set to 2222 for all modules
* Winch side xBee is to be configured as Coordinator, with API mode enabled (no escaping - mode 1)
* Plane side xBees are either routers or endpoints, with API mode enabled (with escaping - mode 2). DH and DL must either 0x000000000000FFFF (broadcast) or set to the Coordinator addresses

# Server side dependencies:

* Python3
* Python modukes: kivy / matplotlib / six / python-xBee (https://github.com/niolabs/python-xbee)
* kivyMD
* kivy-garden.matplotlib
