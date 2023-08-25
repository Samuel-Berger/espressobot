# Welcome to Espressobot

This is a copy of [coffeebot](https://github.com/phixarhasse/coffeebot), fitted to run on a [Raspberry Pi Pico microcontroller](https://www.raspberrypi.com/products/raspberry-pi-pico/).

Responsible for watching the office's coffee maker and sending notifications to a Slack channel and, optionally, lighting Philips Hue lights.

## Hardware Requirements

[Shelly Plug or Plug S](https://www.shelly.cloud/products/shelly-plug-smart-home-automation-device/) for measuring coffeemaker power
and providing access to measurements through its embedded web server.

I recommend the Plug (without the 'S') as it allows for more current through it.

Optional: [Philips Hue Bridge](https://www.philips-hue.com/en-gb/p/hue-bridge/8719514342583) and [Hue Colored Lights](https://www.philips-hue.com/en-gb/products/smart-light-bulbs)

The Hue Bridge has an API through which coffeebot sets the color of all connected lights as follows:

- Red: coffeemaker turned off
- Slowly flashing yellow: coffee is brewing
- Green: coffee is done

## How to Install the Bot

**Note**: The bot is currently calibrated for a Moccamaster KBG744 AO-B (double brewer).

1. Download and unpack the project.
2. Copy `config.py-template` to `config.py`  and adjust the following environment variables in `config.py`:

```sh
USE_SLACK=      # True if you want to send coffee updates to Slack
SLACK_TOKEN=    # Secret OAuth authentication token for the app in Slack (you need to add an app called "CoffeeBot" to your Slack workspace to generate one)
CHANNEL_ID=     # ID of the channel to post messages in Slack
USE_HUE=        # True if you want your Hue lights to reflect coffee status
HUE_IP=         # The local IP address of the Hue Bridge
SENSOR_URL=     # The complete URL to the Shelly Plug, e.g. "http://192.168.0.10/meter/0" without the quotes (see Shelly docs for more details)
```

3. Copy `hue-template` to `hue_username` and change to your username in the file
4. If you chose to use Slack and/or Hue, the script will first setup these services.
During Hue setup, you will be prompted to go press the button on the Hue Birdge to generate a token for the bot to use.
5. Transfer `config.py`, `hue.py`, `main.py` and `slack.py` to Pico W.
This is a [nice guide](https://randomnerdtutorials.com/getting-started-raspberry-pi-pico-w/)
on how to do it from Thonny.

## How to Run the Bot

1. Run it from inside Thonny.
2. Just plug the Pico W into a USB port and it will run `main.py` automatically.

## Development

- [MicroPython docs](https://docs.micropython.org/en/latest/esp32/quickref.html#general-board-control) for the Pico W.
Contains information about (for example) the `machine` and `network` libraries.

## Backlog
See [Issues](https://github.com/phixarhasse/coffeebot/issues)
