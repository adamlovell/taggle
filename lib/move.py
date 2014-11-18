#!/usr/bin/env python

import sys
import os
import shutil
from distutils import dir_util

def move_track (track, track_source, track_dest_dir):
    print('new track destination directory is ', track_dest_dir)
    print('track source is ', track_source)
    print('track is ', track)

    if not os.path.exists(track_dest_dir):
        dir_util.mkpath(track_dest_dir)
    
    if not os.path.exists(track_dest_dir + track):
        shutil.copy(track_source, track_dest_dir)
