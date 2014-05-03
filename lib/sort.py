#!/usr/bin/env python

from lib import tag

def sort_track(track, keys): 

    track_tags = tag.tag(track['source'])
    track_dest_dir = str(track['starting_dir'])

    for value in keys: 
        print value  
        print track_tags[value][0].strip() + '/'
        print track_dest_dir

    track_dest_dir = str('./test_dest_dir/' + track_tags[keys[0]][0] +  '/' + track_tags[keys[1]][0] + '/' + track_tags[keys[2]][0] + '/')

    print (track_dest_dir)
    return track_dest_dir


