#!/usr/bin/env python

import os
import sys 
from distutils import dir_util
from lib import tag
from lib import move 


def sort_track(track, keys): 

    track_tags = tag.tag(track)
    track_dest_dir = str('./test_dest_dir/' + track_tags[keys[0]][0] +  '/' + track_tags[keys[1]][0] + '/' + track_tags[keys[2]][0] + '/')

    print (track_dest_dir)
    move.move_track(track, track_dest_dir)

