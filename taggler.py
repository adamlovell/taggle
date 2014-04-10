#!/usr/bin/env python

import os
import sys 
from distutils import dir_util
from lib import tag
from lib import sort

keys = ['artist', 'album']
new_track = 'src_dir/test.mp3'

track_tags = tag.tag(new_track)
track_dest_dir = str('./' + track_tags[keys[0]][0] + '/' + track_tags[keys[1]][0] + '/')

print (track_dest_dir)
if not os.path.exists(track_dest_dir):
   #os.mkdirs(track_dest_dir)
    dir_util.mkpath(track_dest_dir)

sort.move_track(new_track, track_dest_dir)

