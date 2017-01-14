#! /usr/bin/env python3
import subprocess

"""For py3k images2gif has to be run through 2to3."""


def savegif(infiles, outfile, duration):
    # images = [Image.open(fn) for fn in infiles]

    # size = (150, 150)
    # for im in images:
    #     im.thumbnail(size, Image.ANTIALIAS)
    # print(writeGif.__doc__)
    # print(outfile, images)
    # with open(outfile,'wb') as f:
    #     writeGif(f, images)

    # writeGif(outfile, images)
    cmd = ["convert", "-delay", str(duration * 100)] + infiles + [outfile]

    subprocess.Popen(
        cmd)
    return cmd
