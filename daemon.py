
import os
import subprocess
import requests
import time

while 1:

    output = subprocess.check_output('mocp -i', shell=True).decode('utf-8')

    lines = str(output).split('\n')
    for line in lines:
        if 'File' in line:
            filename = os.path.basename(line)
        if 'Title' in line:
            title = line.replace('Title:', '')
            break

    songname = title if title else filename

    url = 'http://onlinetrackinfo.neochar.com/update.php'
    r = requests.post(url, data={
        'songname': songname,
        'songlength': 313
        })
    print(r.text)

    time.sleep(5)
