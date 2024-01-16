FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python python-dev python-dev python-pip python-venv python-psutil

RUN apt-get install git curl python3-pip ffmpeg -y
ARG USER=root
USER $USER
RUN python -m venv venv
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD bash start
