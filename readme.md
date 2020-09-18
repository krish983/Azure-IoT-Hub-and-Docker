# Publishing Sensor data to Azure IoT Hub

This repository contains Source code, docker file, required dependencies and sample output images.

## Technologies Overview

The following are the technologies that are used in this Application. 

• Python

• Docker

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required dependencies using requirement.txt file

```bash
pip install -r requirements.txt
```

Before running the code change the **connection string** to your ***IoT Hub device conenction string*** in ***.eng file***

## Creating .env file
```bash
### The device connection string to authenticate the device with your IoT hub.
IOTHUB_DEVICE_CONNECTION_STRING = "HostName=<Host Name>;DeviceId=<Device Name>;SharedAccessKey=<Device Key>"
```

## Code Running

```python

python server.py

```

## Docker file  creation

```bash
#----Base Image for python Environment----

FROM python:alpine3.7

#----Copy Files/Build----

COPY . /

#----Create App Directory----

WORKDIR /

#----Dependencies----

RUN pip install -r requirements.txt

#----Run the Application----

CMD python ./server.py

```
## Docker Image bulding and container runnig

```bash

$docker buid --tag python-app .

$docker run --name my-app pyhon-app
```
## Docker useful commands

```bash

$docker image ls

$docker container ls

$docker rm -f "Image_iD"

$dokcer rm -f "container_id"
```

## Important Links

• Python - https://www.python.org/downloads

• Azure IoT Hub Python SDK - https://github.com/Azure/azure-iot-sdk-python

• Docker Tool box for windows - https://docs.docker.com/toolbox/toolbox_install_windows



## Contribution
Krishna Reddy Arikatla
