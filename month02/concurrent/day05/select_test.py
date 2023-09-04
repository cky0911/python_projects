"""
    select示例
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

f = open('log.txt', 'r+')

print("开始监控IO")
# rs, ws, xs = select([s], [f], [])
rs, ws, xs = select([s], [], [])
# <socket.socket fd=336, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8888)>
print(rs)
print(ws)
print(xs)
