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

GRID = 1
SIMPLE = 2

START = ':stable:'
END = ':etable:'


def draw_line(t, row, table, fillchar='-'):
    """
    Draw table line

    :param t: list to append line
    :param table: :class:`Table`
    :param fillchar: character to be filled between `+` signs
    """
    row = row.split()
    t.append('+' + '+'.join(
        (table.max_cell_len(idx) + 2) * fillchar
                             for idx, h in enumerate(row)
    ) + '+')


def put_cells(t, row, table, just='ljust'):
    row = row.split()
    command = '''t.append('|' + '|'.join(
                 (' %s ' % r).{0}(table.max_cell_len(idx) + 2) for idx, r in enumerate(row))
                 + '|')'''.format(just)
    eval(command, {'t': t, 'table': table, 'row': row})


def gen_header(table):
    """
    Formats header accorging to rST

    :params table: :class:`Table`
    :returns: str
    """
    thead = list()
    header = table.header
    draw_line(thead, header, table)
    put_cells(thead, header, table)
    draw_line(thead, header, table, fillchar='=')
    return '\n'.join(thead)


def gen_rows(table):
    trr = list()
    for row in table.rows[1:]:
        put_cells(trr, row, table, just='rjust')
        draw_line(trr, row, table)
    return '\n'.join(trr)


def get_table(source):
    """
    Get table from file
    """
    with open(source, 'r') as f:
        src = f.read()
    start = src.find(START)
    end = src.find(END)
    before = src[:start]
    after = src[end + len(END):]
    table = src[start + len(START):end]
    return table, before, after


def get_rows(table):
    """
    Get rows of given table
    """
    return table.split('\n')[1:-1]


def get_header(rows):
    return rows[0]


def get_structure(source):
    """
    Get structure of table from given source
    """
    table = get_table(source)[0]
    rows = get_rows(table)
    structure = [(i + 1,) for i in range(len(rows))]
    for idx, row in enumerate(rows):
        structure[idx] += (
                           [len(cell)
                            for cell in row.split()
                           ],
        )
    return structure


def max_cell_length(structure, column):
    """
    Get max length of all cells in one column
    """
    return max(row[1][column] for row in structure)


def count_rows(structure):
    """
    Count number of rows in table
    """
    return len(structure)


def count_cols(structure):
    """
    Count number of columns in table
    """
    return len(structure[0][1])


class Table(object):
    """
    Generates table from given source
    """
    def __init__(self, source, type=GRID):
        self.source = source
        self.type = type

    def table(self):
        return get_table(self.source)[0]

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
        return get_rows(self.table())

    def create(self):
        return self.header.to_rst() + '\n' + gen_rows(self)


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


def gen_table(source, type=GRID):
    """
    Tables should be marked as :stable: for start,
    end :etable: for end
    """
    if type == GRID:
        with open(source, 'r') as f:
            fl = f.read()
        start = fl.find(START)
        text_before_table = fl[:start]
        end = fl.find(END)
        text_after_table = fl[end+len(END):]
        text_within = fl[start+len(START):end]
        lines = text_within.split('\n')[1:-1]
        check = lambda: all(len(x.split()) == len(lines[0].split())
                            for x in lines)
        if check:
            header = lines[0].split()
            theader, thead = gen_header(header)
            rows = list()
            for row in lines[1:]:
                rows.append(gen_row(row, thead[0]))
            tr = '\n'.join(rows)
            table = theader + '\n' + tr
            res = text_before_table + table + text_after_table
            with open(source, 'w') as f:
                f.write(res)
            return table
        else:
            print "Check your table!"


if __name__ == '__main__':
    print gen_table('test.rst')

