from flask import Flask, Response
from kafka import KafkaConsumer

consumer = KafkaConsumer('video-topic', bootstrap_servers='kafka:9092')

for message in consumer:
    print(message)

# app = Flask(__name__)


# def kafkastream():
#     for message in consumer:
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + message.value + b'\r\n\r\n')


# @app.route('/')
# def index():
#
#     return "Hello World!"
#
#     # return Response(kafkastream(),
#     #                 mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# if __name__ == '__main__':
#     app.run(debug=True,  host='0.0.0.0')