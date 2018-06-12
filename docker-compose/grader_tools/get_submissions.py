#!/usr/bin/python

import os

course = 'course'

def get_names():
    return os.listdir('/submissions')

def link(name):
    for f in os.listdir(os.path.join('/submissions', name)):
        new_f = f.replace('jovyan', name)
        src = os.path.join('/submissions', name, f)
        tgt = os.path.join('/exchange', course, 'inbound', new_f)
        try:
            os.symlink(src, tgt)
        except:
            print("skipping %s" % src)
        print("%s -> %s" % (f, new_f))

def main():
    for name in get_names():
        link(name)

main()
