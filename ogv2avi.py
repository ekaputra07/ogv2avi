#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Copyright (c) 2012, Eka Putra (ekaputra@balitechy.com)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of the author nor the names of other contributors may
      be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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

