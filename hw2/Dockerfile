FROM python:3.9

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

COPY . ./

CMD [ "python3", "find_mtu.py", "google.com"]