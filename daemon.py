
import os
import subprocess
import requests
import time


def notify_trackinfo():
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

        url = 'http://onlinetrackinfo.neochar.com/update_trackinfo.php'
        r = requests.post(url, data={
            'songname': songname,
            'songlength': 313
            })
    except:
        pass

def notify_activity():
    try:
        with open('activity.txt') as f:
            url = 'http://onlinetrackinfo.neochar.com/update-activity.php'
            r = requests.post(url, data={
                'activity': f.read()
                })

    except:
        pass

    while 1:

        notify_trackinfo()
        notify_activity()

        time.sleep(5)
