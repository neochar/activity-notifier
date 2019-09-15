
import subprocess
import requests
import time

while 1:

    output = subprocess.check_output('mocp -i', shell=True).decode('utf-8')

    lines = str(output).split('\n')
    for line in lines:
        if 'Title' in line:
            title = line.replace('Title:', '')
            break

    if title:
        url = 'http://onlinetrackinfo.neochar.com/update.php'
        r = requests.post(url, data={
            'songname':title, 
            'songlength': 313
            })
        print(r.text)

    time.sleep(5)
