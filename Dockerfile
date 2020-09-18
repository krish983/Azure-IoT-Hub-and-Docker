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