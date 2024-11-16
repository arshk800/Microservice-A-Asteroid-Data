import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

date = input("Enter a date (YYYY-MM-DD):")

#  send message in bytes to server
socket.send(date.encode('utf-8'))

#  Get the reply from server
message = socket.recv()
message = message.decode('utf-8')
print(message)



