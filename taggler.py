#!/usr/bin/env python

from lib import sort

track = 'test_source_dir/test.mp3'
keys = ['genre', 'artist', 'album']

sort.sort_track(track, keys)

'''
track_tags = tag.tag(new_track)
track_dest_dir = str('./test_dest_dir/' + track_tags[keys[0]][0] +  '/' + track_tags[keys[1]][0] + '/' + track_tags[keys[2]][0] + '/')

print (track_dest_dir)
if not os.path.exists(track_dest_dir):
   #os.mkdirs(track_dest_dir)
    dir_util.mkpath(track_dest_dir)

move.move_track(new_track, track_dest_dir)
'''
