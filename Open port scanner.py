import socket

host = str(input("Host:  "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start,end = input("Start: "), input("End: ")
for port in range(int(start),int(end)):
  try:
    s.connect((host, port))
    print("Port open: " + str(port))
    s.close()

  except:
    print("Port closed: " + str(port))
