FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /producer_docker/requirements.txt

WORKDIR /producer_docker

RUN pip install -r requirements.txt

COPY . /producer_docker

ENTRYPOINT [ "python" ]

CMD [ "kafka_video_producer.py" ]