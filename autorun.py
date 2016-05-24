#!/usr/bin/env python3
import os
import time
import subprocess

WATCHED_FILE = 'box.py'
EXECUTE_CMD = 'python3 box.py'

last_mdate = 0.0
while True:
    mdate = os.path.getmtime(WATCHED_FILE)
    if mdate != last_mdate:
        print("------ change detected... running %s:" % (EXECUTE_CMD,))
        subprocess.call(EXECUTE_CMD, shell=True)
        last_mdate = mdate
    time.sleep(0.2)
    
