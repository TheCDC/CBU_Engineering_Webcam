#!/usr/bin/env python3
import time
import shoot
import time_utils
import make_gif
import requests
import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="log/robot.log", level=logging.DEBUG)


def main():
    logging.info("Started.")
    state = 0
    while True:
        try:
            local = time.localtime()
            if local.tm_sec == 0:
                if state == 0:
                    print(time_utils.now())
                    try:
                        logging.debug("Shooting")
                        shoot.shoot()
                    except requests.exceptions.ConnectionError as e:
                        logging.info(e)
                    # render gif
                    # if local.tm_min % 15 == 0:
                    #     make_gif.main()
                    state = 1
            else:
                state = 0
            time.sleep(0.01)

        except (EOFError, KeyboardInterrupt) as e:
            logging.info("Stopped")
            quit()

if __name__ == '__main__':
    main()
