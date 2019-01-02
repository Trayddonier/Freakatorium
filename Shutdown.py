import os
import RPi.GPIO as gp
import time
gp.setmode (gp.BOARD)
gp.setup(13, gp.IN, pull_up_down=gp.PUD_DOWN)
try:
  while True:
    gp.wait_for_edge(13, gp.RISING)
    os.system("System wird heruntergefahren")
    os.system("/sbin/shutdown -h now")
except: gp.cleanup()
