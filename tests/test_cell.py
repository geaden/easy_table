# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from base import BaseTableTestCase
from rstable.utils import max_cell_length


class CellsTestCase(BaseTableTestCase):
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