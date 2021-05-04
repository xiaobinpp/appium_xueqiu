# -*- coding: utf-8 -*-
import os
import shlex
import signal
import subprocess
import time


# def test_video():
#     # cmd = shlex.split("scrcpy --record a.mp4")
#     # p = subprocess.Popen(cmd,shell=False)
#     # time.sleep(10)
#     # os.kill(p.pid,signal.SIGTERM)
#
#     # cmd = "scrcpy --record a.mp4"
#     # p = os.popen(cmd)
#     # time.sleep(10)
#     # os.kill(p.pid,signal.CTRL_C_EVENT)


def test_vedio():
    cmd=shlex.split("scrcpy")
    cmd1 = "uiautomatorviewer.bat"
    cmd2 = 'pwd'
    p = subprocess.Popen(cmd, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    f = p.stdout.read()
    # print(f.decode('utf-8'))
    print(p.pid)
    print(f)
    time.sleep(10)
    os.kill(p.pid, signal.CTRL_C_EVENT)


