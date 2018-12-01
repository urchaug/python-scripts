# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:00:07 2018

@author: Urchaug
"""

from time import clock

class stopwatch:
    def _init_(self):
        self.reset()
    def start(self):  # start the timer
        if not self._running:
            self._start_time = clock()
            self._running = True
        else:
            print("stopwatch already running")
            
            
    def stop(self):
        if self._running:
            self._elapsed += clock() - self._start_time
            self._running = False
        else:
            print("stopwatch not runnuing")
            
    def reset(self):
        self._start_time = self._elapsed = 0
        self._running = False
    def elapsed(self):
        if not self._running:
            return self._elapsed
        else:
            print("stopwatch must be stopped")
            return None
        