#!/usr/bin/env python

import sys
import os
from pprint import pprint
from mutagen.easymp4 import EasyMP4
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3


def tag (track):
    tagged_track = track_tags(track_extention(track))
    return tagged_track

def track_extention (track):
    if os.path.splitext(track)[1] == '.mp3':
        new_track = MP3(track, ID3 = EasyID3)
    if os.path.splitext(track)[1] == '.m4a':
        new_track = EasyMP4(track)
    return new_track


def track_tags (track):
    track.title = track['title'][0]
    track.artist = track['artist'][0]
    track.album = track['album'][0]
    track.genre = track['genre'][0]
    return track
