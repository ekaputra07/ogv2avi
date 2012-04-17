#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog -i [video_input.ogv] -o [video_output.avi]")

    parser.add_option(
        "-i", "--input",
        action="store",
        dest="input",
        default=False,
        help="OGV file input"
        )

    parser.add_option(
        "-o", "--output",
        action="store",
        dest="output",
        default=False,
        help="AVI file output name"
        )

    options, args = parser.parse_args()

    if not options.input:
        parser.error("Ogv file not specified")

    if not options.output:
        parser.error("AVI output file name not specified")

    return options

def convert(v_input, v_output):
    command = 'mencoder %s -o %s -oac mp3lame -lameopts fast:preset=standard -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=4000' % (
        v_input,
        v_output)

    os.system(command)
    return

if __name__ == '__main__':
    opts = main()
    convert(opts.input, opts.output)
    raw_input('Press [ENTER] to continue...')

