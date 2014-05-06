#!/usr/bin/env python

def sort_track(track, keys): 

    track_dest_dir = str(track['starting_dir'])
    for value in keys: 
        track_dest_dir += track['tags'][value][0].strip() + '/'

    print (track_dest_dir)
    return track_dest_dir


