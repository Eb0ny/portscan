# coding=utf-8

import time,sys
import socket
import queue
import threading
#123

class PortScaner(object):
    """
    类的使用，多线程的使用
    """

    class PortScan(threading.Thread):
        def __init__(self, portQueue, ip, timeout):
            """
            初始化
            """
            threading.Thread.__init__(self)
            self.portQueue = portQueue
            self.ip = ip
            self.timeout = timeout

        def run(self):
            while True:
                if self.portQueue.empty():
                    break
                OPEN_MSG = "% 6d [OPEN]\n"
                port = self.portQueue.get(timeout=0.5)
                ip = self.ip
                timeout = self.timeout

                try:
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.settimeout(timeout)
                    resultCode = s.connect_ex((ip,port))
                    if resultCode == 0:
                        sys.stdout.write(OPEN_MSG % port)

