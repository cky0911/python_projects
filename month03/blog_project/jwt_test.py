import base64
import json
import time
import copy
import hmac


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def b64encode(content):
        return base64.urlsafe_b64encode(content).replace(b'=', b'')

    @staticmethod
    def b64decode(b):
        rest = len(b) % 4
        if rest > 0:
            b += b'=' * (4 - rest)
        return base64.urlsafe_b64decode(b)

    @staticmethod
    def encode(payload, key, exp=300):
        # init header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        # init payload
        payload_self = copy.deepcopy(payload)
        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError("the param of exp must be int or str.")
        payload_self['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_self, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # init sign
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        sign_bs = Jwt.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' + sign_bs

    @staticmethod
    def decode(token, key):
        # 校验签名
        # 检查exp是否过期
        # return payload部分的解码
        header_bs, payload_bs, sign_bs = token.split(b'.')
        # 校验sign_bs
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        # 比对
        if sign_bs != Jwt.b64encode(hm.digest()):
            raise
        # 检查是否过期
        payload_json = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_json)

        if 'exp' in payload:
            now = time.time()
            if now > payload['exp']:
                raise
        return payload


if __name__ == "__main__":
    token = Jwt.encode({'uname': 'zyy'}, '123456', 300)
    print("generate  token as follows: " + str(token))
    print("compare result: " + str(Jwt.decode(token, '123456')))
