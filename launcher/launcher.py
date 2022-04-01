#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


print("start python script")
subprocess.call(["python.exe", "./hello.py"])
print("end python script\n")


print("start bash script")
subprocess.call(["bash", "./hello.sh"])
print("end bash script")
