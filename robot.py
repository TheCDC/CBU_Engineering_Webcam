#! /usr/bin/env python3
import time
import shoot
import time_utils
import make_gif


def main():
    state = 0
    while True:
        try:
            local = time.localtime()
            if local.tm_sec == 0:
                if state == 0:
                    print(time_utils.now())
                    shoot.shoot()
                    if local.tm_min % 15 == 0:
                        make_gif.main()
                    state = 1
            else:
                state = 0

        except (EOFError, KeyboardInterrupt):
            print("Quitting...")
            quit()

if __name__ == '__main__':
    main()
