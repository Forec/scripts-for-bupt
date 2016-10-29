#coding=utf-8
__author__ = 'Forec'
import time
import sys
import urllib
import urllib2
import cookielib
import threading
  
if len(sys.argv) != 3:
	print "Usage: python2 login.py <id> <pwd>"
	sys.exit(0)
else:
	username = sys.argv[1]
	password = sys.argv[2]

postdata=urllib.urlencode({
    'DDDDD': username,
    'upass': password,
    'savePWD':'0',
    '0MKKey':''
})

class LoginThread(threading.Thread):
    def __init__(self, postdata, url):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.url = url
        self.postdata = postdata
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
    def run(self):
        req = urllib2.Request(
            url = self.url,
            data = self.postdata
        )
        self.opener.open(req)

dorm = LoginThread(postdata, "http://10.3.8.211")
teach = LoginThread(postdata, "http://10.4.1.2")

teach.start()
time.sleep(1)
if teach.isAlive():
    dorm.start()
    time.sleep(2)