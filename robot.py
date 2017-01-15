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
    # intialize simple state machine to handle timing
    state = 0
    while True:
        try:
            local = time.localtime()
            # only shoot on the bottom of each minute
            if local.tm_sec == 0:
                # don't shoot multiple times per second
                if state == 0:
                    print(time_utils.now())
                    # shoot first
                    try:
                        logging.debug("Shooting")
                        shoot.shoot()
                    # ask questions later
                    except requests.exceptions.ConnectionError as e:
                        logging.info(e)
                    state = 1
            else:
                state = 0
            # delay to avoid wasting CPU cycles
            time.sleep(0.01)
        # handle user-requested termination
        except (EOFError, KeyboardInterrupt) as e:
            logging.info("Stopped")
            quit()

if __name__ == '__main__':
    main()
