#!/usr/bin/env python

import sys
import os
import shutil

def move_track (track, destination_directory):
    print(track, destination_directory);
    
    shutil.copy(track, destination_directory)
