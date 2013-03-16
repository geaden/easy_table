# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from config import GRID
from utils import (get_table, get_structure,
                   max_cell_length, gen_rows,
                   gen_header, get_rows)


class Table(object):
    """
    Generates table from given source
    """
    def __init__(self, source, type=GRID):
        self.source = source
        self.type = type

    def table(self):
        table = get_table(self.source)[0]
        return table

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__,
                            self.table()
        )

    def __str__(self):
        return self.table()

    def structure(self):
        """
        Structure of table
        """
        return get_structure(self.source)

    def max_cell_len(self, column):
        return max_cell_length(self.structure(), column)

    @property
    def header(self):
        return Header(self)

    @property
    def rows(self):
        rows = get_rows(self.table())
        check = lambda: all(len(x.split()) == len(self.header.split())
                            for x in rows)
        if check:
            return rows
        raise ValueError("Please check your table. You have different number"
                         "of columns for each row of the table")

    def create(self):
        return self.header.to_rst() + gen_rows(self)


class Header(object):
    """
    Header class
    """
    def __init__(self, table):
        self.table = table
        self.header = table.rows[0]

    def __str__(self):
        return self.header

    def __repr__(self):
        return self.__str__()

    def split(self):
        return self.header.split()

    def to_rst(self):
        return gen_header(self.table)
