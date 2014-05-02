#!/usr/bin/env python

import sys
import os
import shutil
from distutils import dir_util

def move_track (track, track_dest_dir):
    print(track, track_dest_dir)

    if not os.path.exists(track_dest_dir):
        dir_util.mkpath(track_dest_dir)

    shutil.copy(track, track_dest_dir)
