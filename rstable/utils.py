# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from config import START, END


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
    """
    Generate rows in rSt format

    :param table: :class:`Table`
    :return: formatted rows
    """
    trr = list()
    for row in table.rows[1:]:
        put_cells(trr, row, table, just='rjust')
        draw_line(trr, row, table)
    return '\n' + '\n'.join(trr)


def get_table(source):
    """
    Get table from file
    """
    with open(source, 'r') as f:
        src = f.read()
    start = src.find(START)
    end = src.find(END)
    if not start or end:
        raise ValueError("Please check your source")
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
