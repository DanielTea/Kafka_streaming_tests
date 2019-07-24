import time
import sys
import cv2

from kafka import KafkaProducer
from kafka.errors import KafkaError

# producer = KafkaProducer(bootstrap_servers='kafka:29092')
# topic = 'video-topic'

# def emit_video(path_to_video):
#     print('start emitting')
#
#     video = cv2.VideoCapture(0)
#
#     while True:
#         success, frame = video.read()
#         if not success:
#             break
#
#         # png might be too large to emit
#         data = cv2.imencode('.jpeg', frame)[1].tobytes()
#
#         future = producer.send(topic, data)
#
#         try:
#             future.get(timeout=10)
#
#         except KafkaError as e:
#             print(e)
#             break
#
#         print('.', end='', flush=True)
#
#     video.release()
#
#     print('done')
#
#
# if __name__ == '__main__':
#     emit_video()

print("stuff")