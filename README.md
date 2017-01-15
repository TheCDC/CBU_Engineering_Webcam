# CBU_Engineering_Webcam

A set of tools to save the webcam feed at http://engineeringwebcam.calbaptist.edu/ and create timelapse gifs.

# Dependencies #

Python
```
requests
```

Command Line Utilities
```
convert # ImageMagick
```

# Usage #
Execute `robot.py` to capture a frame every minute with frames save in `frames/`.

Execute `make_gif.py` to turn all captured frames into a gif. This depends on the ImageMagick command line tool on *nix systems. Defaults to 1 frame/15 minutes at 20 fps.

Executer `shoot.py` to capture a single frame into `frames/`.
