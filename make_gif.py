#!/usr/bin/env python3
import savegif
import os
import time_utils
def main():
    paths = []
    for fname in os.listdir("frames/"):
        paths.append(os.path.abspath(os.path.join(
            "frames", fname)))
    # print(paths)
    savegif.savegif(paths, "gifs/ani.gif", 0.25)

if __name__ == '__main__':
    main()