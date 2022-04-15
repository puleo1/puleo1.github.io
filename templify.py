#!/usr/bin/env python3

import sys
import string

def do_template(cprefix):
    cfile = open("%s.template" % cprefix)
    content = cfile.read()
    cfile.close()

    tfile = open("template.html")
    template = string.Template(tfile.read())
    tfile.close()
    
    filled = template.substitute(content=content)

    ofile = open("%s.html" % cprefix, "w")
    ofile.write(filled)
    ofile.close()

def main():
    if len(sys.argv) < 2:
        print("usage: %s contentprefix [contentprefix ...]" % sys.argv[0])
        return

    for n in range(1, len(sys.argv)):
        cprefix = sys.argv[n]
        do_template(cprefix)

if __name__ == '__main__':
    main()
