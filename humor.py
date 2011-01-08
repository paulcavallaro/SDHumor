#!/usr/bin/python
import sys

def humor(fname) :
    fd = open(fname)
    last_line = None
    for line in fd :
        if last_line and "def" in last_line[:3] :
            print "    raise DeprecationWarning(\"I'm really not THAT funny.\")"
        print line,
        last_line = line

if __name__ == '__main__' :
    humor(sys.argv[0])
