"""
    httpserver 3.0
    1.获取http请求
    2.解析http请求
    3.将请求发送给WebFrame
    4.从WebFrame接收反馈数据
    5.将数据组织为Response格式发送给客户端
"""

from socket import *
from threading import Thread
import json, re
from config import *  # 导入配置文件内容


# 负责和webframe交互, socket客户端
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return

    # 将env转换为json发送
    data = json.dumps(env)
    s.send(data.encode())
    # 接收webframe反馈的数据
    data = s.recv(1024 * 1024 * 10).decode()
    return json.loads(data)


# httpserver功能
class HTTPServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)

    # 绑定地址
    def bind(self):
        self.address = (self.host, self.port)
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Start the http server:%d" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("connect from:%d" % addr)
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 具体处理客户端请求
    def handle(self, connfd):
        # 获取HTTP请求
        request = connfd.recv(4096).decode()
        # print(request)
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            # groupdict 获取捕获组名：内容  得到字典
            env = re.match(pattern, request).groupdict()
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            # data就是从webframe得到的数据
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 负责给浏览器发送数据
    def response(self, connfd, data):
        # data-->{'status':'200','data':'xxx'}
        if data['status'] == '200':
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += 'Content-Type:text/html\r\n'
            response_headers += '\r\n'
            response_body = data['data']
        elif data['status'] == '404':
            response_headers = "HTTP/1.1 404 Not Found\r\n"
            response_headers += 'Content-Type:text/html\r\n'
            response_headers += '\r\n'
            response_body = data['data']
        elif data['status'] == '302':
            pass

        # 将数据发送给浏览器
        # 这也能打印出来。。。
        data = response_headers + response_body
        connfd.send(data.encode())


if __name__ == '__main__':
    httpd = HTTPServer()
    # 启动服务
    httpd.serve_forever()
