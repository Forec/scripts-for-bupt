#coding=utf-8
__author__ = 'Forec'
import time
import sys
import urllib
import urllib2
import cookielib
import threading

class LogoutThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.url = url
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
    def run(self):
        req = urllib2.Request(
            url = self.url
        )
        self.opener.open(req)

dorm = LogoutThread("http://10.3.8.211/F.html")
teach = LogoutThread("http://10.4.1.2/F.html")

teach.start()
time.sleep(1)
if teach.isAlive():
    dorm.start()
    time.sleep(1)