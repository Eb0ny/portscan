import whois, pprint
import socket
import os


def ipWhois(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('whois.apnic.net', 43))
    s.send(ip.encode('utf-8') + b'\r\n')
    result = bytearray()
    while True:
        data = s.recv(10000)
        if not len(data):
            break
        result.extend(data)
    s.close()
    result = result.decode('ascii')
    # print(result)
    # print(type(result))
    filename = ip + '.txt'
    f = open(filename, 'wb')
    f.write(result.encode('utf-8'))
    f.close()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    print('查询结果 ' + file_path)


def urlWhois(url):
    data = whois.whois(url)
    pprint.pformat(data)
    filename = url + '.txt'
    data = str(data)
    # print(data)
    f = open(filename, 'wb')
    f.write(data.encode('utf-8'))
    f.close()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    print('查询结果 ' + file_path)


