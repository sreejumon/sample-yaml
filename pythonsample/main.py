import time
# import socket
import traceback
from connection import connections

if __name__ == "__main__":
    while True:
        try:
            time.sleep(5)
            print("Reading the information from Redis")
            client = connections.get_client()
            print("Reading the value for hello ", client.get("hello"))
#             port = socket.getservbyname("redis-main-service-1")
#             print("The port received is ", port)
        except Exception:
            traceback.print_exc()
