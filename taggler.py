#!/usr/bin/env python

import sys 
from lib import tagger
from lib import sorter

TEST_TRACK = 'src_dir/test.mp3'
SORT_BY = 'artist'

#print(tagger.tag('src_dir/test.mp3').title)
#print(tagger.tag('src_dir/test.m4a').title)

new_track_tag = tagger.tag(TEST_TRACK)
new_track_dest_dir = str(new_track_tag[SORT_BY][0] + '/')

sorter.move_track(TEST_TRACK, new_track_dest_dir)

#print(new_track[SORT_BY][0] + '/')
