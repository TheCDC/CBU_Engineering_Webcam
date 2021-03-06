#!/usr/bin/env python3
import time
import shoot
import time_utils
import requests
import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="log/robot.log", level=logging.INFO)


def main():
    logging.info("Started")
    # intialize timer to ensure correct time in between shots.

    try:
        # wait until the beginning of the next minute
        while time.localtime().tm_sec != 0:
            time.sleep(0.01)

        while True:
            # only shoot on the bottom of each minute
            while time.localtime().tm_sec != 0:
                time.sleep(0.01)
            # don't shoot multiple times per second
            print(time_utils.now())
            # shoot first
            try:
                logging.info("Shooting")
                shoot.shoot()
            # ask questions later

            except (KeyboardInterrupt, EOFError) as e:
                raise e
            except requests.exceptions.ConnectionError as e:
                logging.warning(e)
                print(e)
            except Exception as e:
                logging.warning(e)
                raise e
            # delay to avoid wasting CPU cycles
    except (EOFError, KeyboardInterrupt) as e:
        # handle user-requested termination
        logging.info("Stopped")
        quit()

if __name__ == '__main__':
    main()
