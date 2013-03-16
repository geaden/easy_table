# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

"""
Generates rst table from provided source
"""
import os
import sys

import time
from config import GRID
from rstable import Table
from rstable.utils import get_table

VERSION = '1.0.1'
HELP = """    Create rst tables with ease

    Usage:
    easy_table.py [OPTIONS] source

    source - file contains future table marked with :stable: and :etable: tags

    OPTIONS
        -h, --help  show this help
        -v          show version
        --verbose   verbose generating table
"""

def create_table(source, type=GRID, verbose=False):
    """
    Main function to modify your rst file
    with table
    """
    table = Table(source, type)
    before, after = get_table(source)[1:]
    rstable = table.create()
    start = time.time()
    print "Start generating table from %s" % source
    if verbose:
        print rstable
    with open(source, 'w') as f:
        f.write(before +
                rstable +
                after)
    print "Table has been successfully generated in %f seconds" % (time.time() - start)

if __name__ == '__main__':
    if not sys.argv[1:]:
        print HELP
    if sys.argv[1].startswith('-'):
        if '-h' in sys.argv[1] or '--help' in sys.argv[1:]:
            print HELP
        elif '--verbose' in sys.argv[1]:
            source = sys.argv[2]
            create_table(source, verbose=True)
        elif '-v' in sys.argv[1]:
            print 'Easy table: %s' % VERSION
        else:
            print HELP
    else:
        try:
            source = os.path.abspath(sys.argv[1])
            create_table(source)
        except IOError, e:
            print "%s" % e
