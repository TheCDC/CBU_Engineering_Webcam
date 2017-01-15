#!/usr/bin/env python3
import savegif
import os
import time_utils

frames_divisor = 15

def main():
    paths = []
    for fname in os.listdir("frames/"):
        paths.append(os.path.abspath(os.path.join(
            "frames", fname)))
    # print(paths)
    paths.sort()
    savegif.savegif(paths[::frames_divisor], "gifs/ani.gif", 0.05)

if __name__ == '__main__':
    main()
