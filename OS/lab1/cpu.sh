#!/bin/bash
sudo apt-get install stress-ng

stress-ng --cpu 1 --timeout 60s --cpu-method callfunc