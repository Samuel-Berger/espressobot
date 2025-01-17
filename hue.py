import os
import urequests
import config
from time import sleep

class Hue:
    def __init__(self):
        try:
            self.useHue = config.USE_HUE
            self.bridgeIp = config.HUE_IP
            #self.username = config.HUE_USERNAME
            self.url = f"http://{self.bridgeIp}/api"
        except KeyError:
            print("Could not parse USE_HUE or HUE_IP in the file .env")
            quit()
            
        self.lights = []
        self.loadUsername()
        self.username = config.HUE_USERNAME
        if(self.username == ""):
            print("Waiting for Hue authorization...")
            self.authorize()
            print("---> Hue Authorization complete!")

    def saveUsername(self, username):
        try:
            f = open("hue_username", "w")
            f.write(username)
            f.close()
        except Exception as e:
            print(e)
    
    def loadUsername(self):
        try:
            f = open("hue_username", "r")
            self.username = f.readline()
            f.close()
        except Exception as e:
            print(e)
            self.username = ""
            return

    def authorize(self):
        self.username = ""
        try:
            hueResponse = urequests.post(self.url, json={"devicetype": "espressobot"})
            if(hueResponse.json()[0]["error"]["type"] == 101): # Need to generate username
                print("Please press the link button on the HUE Bridge.")
                user_input = input("Have you pressed it? [y/n] ")
                if(not user_input == 'y'):
                    print("Error during Hue authentication. Exiting.")
                    exit(1)
                else:
                    hueResponse = urequests.post(self.url, json={"devicetype": "espressobot"})
                    username = hueResponse.json()[0]["success"]["username"]
                    self.username = username
                    self.saveUsername(username)
            elif(hueResponse.status_code == 200):
                username = hueResponse.json()[0]["success"]["username"]
                self.username = username
                self.saveUsername(username)
        except Exception as e:
            print("Error during Hue authentication.")
            print("Exception: ", e)
            return

    def getLights(self):
        print('Getting Hue lights...')
        self.lights = []
        if(self.username == ""):
            return
        try:
            hueResponse = urequests.get(f"{self.url}/{self.username}/lights/")
            if(not hueResponse.status_code == 200):
                print("Unable to get Hue lights.")
                return
        except Exception as e:
            print(e)
            return
        for light in hueResponse.json():
            print('Adding light {}' .format(light))
            self.lights.append(light)
        return
    
    def setAllLights(self, color):
        try:
            for light in self.lights:
                hueResponse = urequests.put(
                    f"{self.url}/{self.username}/lights/{light}/state",
                    json={"on":True, "sat": 254, "bri":200, "hue": color})
                #print(f"Hue light {light}: {hueResponse.status_code}")
                sleep(0.5)
        except Exception as e:
            print(e)
            return
    
    def turnOffAllLights(self):
        try:
            for light in self.lights:
                hueResponse = urequests.put(
                    f"{self.url}/{self.username}/lights/{light}/state",
                    json={"on":False})
                #print(f"Hue light {light}: {hueResponse.status_code}")
                sleep(0.5)
        except Exception as e:
            print(e)
            return

