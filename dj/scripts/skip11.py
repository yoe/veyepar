#!/usr/bin/python

# push encoded files to apu.debconf.org.
# uses rsync.

import os, subprocess

from process import process
from main.models import Show, Location, Episode

class skip(process):

    ready_state = None
    ret = None

    def set_ready(self, state):
        self.ready_state = state
    def process_ep(self, ep):
        return True

if __name__ == '__main__':
    p=skip()
    p.set_ready(11)
    p.main()

