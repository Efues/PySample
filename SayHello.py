#!/usr/bin/env python
import sys
from time import sleep

if __name__ == '__main__':
    sys.stdout = open('/dev/console', 'w')
    while True:
        print "Hello world %s" % (sys.argv)
        sys.stdout.flush()
        sleep(1)
