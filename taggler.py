#!/usr/bin/env python

from lib import sort
from lib import move

track = {}
track['source'] = 'test_source_dir/test.mp3'
track['starting_dir'] = './test_dest_dir/'
keys = ['genre', 'artist', 'album'] 
track['destination_dir'] = sort.sort_track(track, keys)
move.move_track(track['source'], track['destination_dir'])
