#!/usr/bin/env python

import sys
import os
import shutil

def move_track (track, dest_dir):
    shutil.copy(track, dest_dir)
    print(dest_dir)

    
