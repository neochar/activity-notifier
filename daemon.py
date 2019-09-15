
import os
import subprocess
import requests
import time

while 1:

    try:
        output = subprocess.check_output('mocp -i', shell=True).decode('utf-8')

        lines = str(output).split('\n')
        for line in lines:
            if 'File' in line:
                filename = os.path.basename(line).strip()
            if 'Title' in line:
                title = line.replace('Title:', '').strip()
                break

        songname = title if title else filename

        url = 'http://onlinetrackinfo.neochar.com/update.php'
        r = requests.post(url, data={
            'songname': songname,
            'songlength': 313
            })
    except:
        pass

    time.sleep(5)
