import socket
import sys
from time import sleep

# 服务端主机IP地址和端口号
HOST = "127.0.0.1"
PORT = 2328

# 使用IPV4协议，使用tcp协议传输数据
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 连接服务器
    s.connect((HOST, PORT))
except Exception as e:
    print('找不到服务器，请稍后重试！')
    sys.exit()
while True:
    c = input('请输入你想发送的消息：')
    # 发送数据，使用UTF-8编码成字节码
    s.sendall(c.encode())
    # 从服务端接收数据，大小最多为1024比特
    data = s.recv(1024)
    # 解码
    data = data.decode()
    print('收到回复：', data)
    if c.lower() == 'bye':
        sleep(1)
        break
# 关闭连接
s.close()