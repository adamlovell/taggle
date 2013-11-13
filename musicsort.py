#!/usr/bin/env python

import sys 
from lib import tagger

print(tagger.tag('test.mp3').title)
print(tagger.tag('test.m4a').title)
