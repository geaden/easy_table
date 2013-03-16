# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import unittest
from rstable import Table
from rstable.utils import get_structure


class BaseTableTestCase(unittest.TestCase):
    def setUp(self):
        source = 'test.rst'
        self.structure = get_structure(source)
        self.table = Table(source)
