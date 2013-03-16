# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import unittest
from easy_table import (get_structure, count_rows,
                        count_cols, max_cell_length,
                        Table)


class TableTestCase(unittest.TestCase):
    def setUp(self):
        source = 'test.rst'
        self.structure = get_structure(source)
        self.table = Table(source)
        self.source = source

    def testGetTableStructure(self):
        self.assertEqual(
            [
                (1, [2, 4, 4]),
                (2, [1, 1, 4]),
                (3, [1, 1, 2]),
                (4, [1, 1, 3])
            ],
            self.structure
        )

    def testCountRows(self):
        rows = count_rows(self.structure)
        self.assertEqual(
            4,
            rows
        )

    def testCountCols(self):
        cols = count_cols(self.structure)
        self.assertEqual(
            3,
            cols
        )

    def testMaxLen(self):
        self.assertEqual(
            4,
            max_cell_length(self.structure, 2)

        )
        self.assertEqual(
            4,
            max_cell_length(self.structure, 1)
        )
        self.assertEqual(
            2,
            max_cell_length(self.structure, 0)
        )

    def testTableAsClass(self):
        """
        Test case for easy table Table class
        """
        self.assertEqual(
            self.structure,
            self.table.structure()
        )

    def testTableHeader(self):
        self.assertEqual(
            'id code name',
            self.table.header.__str__()
        )

    def testRstTableHeader(self):
        self.assertEqual(
            '''
            +----+------+------+
            | id | code | name |
            +====+======+======+
            ''',
            self.table.header.to_rst()

        )
