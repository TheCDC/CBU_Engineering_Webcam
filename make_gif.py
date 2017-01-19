#!/usr/bin/env python3
import savegif
import os
import time_utils

frames_divisor = 15


def main():
    paths = [os.path.abspath(os.path.join(
        "frames", fname)) for fname in os.listdir("frames/")]
    paths.sort()
    # print(paths)
    savegif.savegif(paths[::frames_divisor], "gifs/ani.gif", 1/10)

if __name__ == '__main__':
    main()
