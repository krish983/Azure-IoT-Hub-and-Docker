#Dependencies for this Application
import os
import random
import time
from datetime import datetime
import pytz #For time Zone Selection
from dotenv import load_dotenv  #For loading env data
import logging  #Logging and debugging

from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse    #Python Device SDK for IoT Hub:

project_folder = os.path.expanduser(os.getcwd())  #Adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))   #Load connectuion string of IoT Hub Service

# The device connection string to authenticate the device with your IoT hub.
connection_string = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

time_zone = pytz.timezone('America/Los_Angeles')
intervel = 1    #Adjust to delay in each message publish to IoT Hub

#Logging of messages to external file
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \ :: %(message)s', level = logging.INFO, filename = 'datalogs.log', filemode = 'w')

#IoT Hub connection 
def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    return client

#Data Processing and Publishing to IoT Hub
def iothub_client_data_run():
    try:
        client = iothub_client_init()
        print("Sending messages to IoT Hub periodically , press Ctrl-C to exit")

        while True:
            current_time = int(time.time()) #Current time in unix format
            iso_time = datetime.fromtimestamp(current_time, time_zone).isoformat()  #Current time in ISo Format
            sensor_value = sensor_values(random.uniform(1.0, 10.0)) #Random value computation for sensor value 
            quality_code = random.randint(0, 2) #Random Value for quality code between(0,2)
            device_id = str(random.randint(1, 4))   #Random Value for device ID between(0,2)
            
            # Define the JSON message to send to IoT Hub.
            data = {
                "header": {
                "ConfigVersion": 13,  # version of the app
                "GroupID": "EDGE",  # cloud tenant
                "LandingPoint": "Edge",  # bus configuration
                "MessageID": 1606287844,  # unique message id
                "MessageType": "IODataReport",  # Data format type
                "SrcModule": "your-python-edge-app",  # source module info
                "TimeStamp": current_time  # Unix timestamp
                },
                "timestamp": iso_time,  # ISO timestamp
                "device": [
                    {
                        "id": device_id,
                        "tags": {
                            "Sensor 1": {
                                "quality_code": quality_code,
                                "timestamp": current_time,
                                "value": sensor_value
                            },
                            "Sensor 2": {
                                "quality_code": quality_code,
                                "timestamp": current_time,
                                "value": sensor_value
                          }
                        }
                      },
                      {
                          "id": device_id,
                          "tags": {
                              "Sensor 3": {
                                  "quality_code": quality_code,
                                  "timestamp": current_time,
                                  "value": sensor_value
                              },
                              "Sensor 4": {
                                  "quality_code": quality_code,
                                  "timestamp": current_time,
                                  "value": sensor_value
                              }
                          }
                      }
                  ]
              }

            # Send the message.
            print("Sending message: {}".format(data))
            logging.info('Sending Message to IoT Hub: {}'.format(data)) #Data Logging
            client.send_message(str(data))  #Data Publish to IoT Hub
            print("Message sent")
            time.sleep(intervel)

    except KeyboardInterrupt:
        print("Application stopped")

#Compute Sensor value and Applied Unit test on this
def sensor_values(value):
    sensor_data = value**3
    return sensor_data

#Main method and program start from here   
if __name__ == '__main__':
    print("IoT Sensor Data Simulation")
    print("Press Ctrl-C to exit")
    iothub_client_data_run() #Method calling