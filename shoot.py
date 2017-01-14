#! /usr/bin/env python3
import requests
import time_utils

target = "http://engineeringwebcam.calbaptist.edu/nph-jpeg.cgi?0&1484333436119382"


def shoot(dest="frames"):
    response = requests.get(target)
    fname = time_utils.now()
    with open("{}/{}.jpg".format(dest, fname), 'wb') as f:
        f.write(response.content)


def main():
    shoot()

if __name__ == '__main__':
    main()
