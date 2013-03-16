# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from base import BaseTableTestCase
from rstable.utils import count_rows, count_cols


class TableTestCase(BaseTableTestCase):
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
            '+----+------+------+\n| id | code | name |\n+====+======+======+',
            self.table.header.to_rst()
        )

    def testCreateTable(self):
        self.assertEqual(
            """+----+------+------+
| id | code | name |
+====+======+======+
|  1 |    2 | test |
+----+------+------+
|  2 |    3 |   py |
+----+------+------+
|  3 |    4 |  sub |
+----+------+------+""",
            self.table.create()
        )
