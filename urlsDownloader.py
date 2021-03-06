import os
import sys
import requests
import urllib.request
import random
import time
from utils.header import requests_headers

def download_image(url, filename, file_in, lineNo):
    file_out = filename + '.jpg'
    log_out = file_in + '.log'
    cwd = os.getcwd()
    hdr = requests_headers()

    try:
        raw = requests.get(url, headers=hdr)
        with open(os.path.join(os.getcwd(), 'PHOTO_NET_2', file_out), 'wb') as image:
            image.write(raw.content)
        time.sleep(0.5) # Maybe wait for a longer time until connecting to the url?
        return False

    except requests.exceptions.RequestException as err:
        print(err)
        with open(log_out, 'a') as log:
            log.write(filename)
            log.write(' ')
            log.write(url)
            log.write(' ')
            log.write(str(lineNo))
            log.write(' ')
            log.write(str(err))
        return True

if __name__ == '__main__':
    file_in = 'NETmen_urls'
    lineNo = 0

    f = open(file_in, 'r')
    for line in f:
        # if lineNo < 1906:
        #     lineNo += 1
        #     continue
        # Since last time it fails at line 1906

        file_out, url = line.strip('\n').split()
            
        exceptionRaise = download_image(url, file_out, file_in, lineNo)
            
        if exceptionRaise:
            print("Exception Raise at line {}. Halt from {} for 1800 secs".format(lineNo, time.strftime("%H:%M:%S", time.localtime())))
            time.sleep(1800)
        elif (lineNo % 100) == 0 and lineNo != 0: # Sleep for an hour for every 100 photos
            print("At line {}. Halt from {}  for 600 secs".format(lineNo, time.strftime("%H:%M:%S", time.localtime())))
            time.sleep(600)
        elif (lineNo % 20) == 0 and lineNo != 0: # Sleep for a while for every 20 photos
            var = random.randrange(30, 60)
            print("At line {}. Halt for {} secs".format(lineNo, var))
            time.sleep(var)
        lineNo += 1
    f.close()
    print('Finished!')
            
        