#!/usr/bin/env python

import os
from lib import sort
from lib import move
from lib import tag

tracks = []
keys = ['genre', 'artist', 'album'] 
#rootdir = './test_source_dir'
rootdir = '/Volumes/Macintosh\ HD/Users/adam.lovell/Desktop/music_test'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        track = {}
        track['source'] = subdir + '/' + file
        track['base_dir'] = './test_dest_dir/'
        track['tags'] = tag.tag(track['source'])
        track['destination_dir'] = sort.sort_track(track, keys)
        move.move_track(file, track['source'], track['destination_dir'])
