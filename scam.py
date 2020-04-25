import requests
import os
import random
import string
import json
import sys
import time

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
if len(sys.argv) > 1:
    url = sys.argv[1]
    uname = sys.argv[2]
    pw = sys.argv[3]
else:
    url = None
    pass
names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))

    if url != None:
         requests.post(url, allow_redirects=False, data={
             '%s' % (uname): username,
             '%s' % (pw): password
         })

         print 'sent %s, %s to %s in fields %s and %s' % (username, password, url, uname, pw)
    elif url == None:
        print 'Would have sent username \"%s\" and password \"%s\"' % (username, password)
