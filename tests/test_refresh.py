# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import os
import sys
import shutil
import logging
from hovertools import command_line
from .config import TMP_REPO_DIR
from hovertools.utils import ensure_repo_exists


sys.exit = lambda *x: None
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
root = logging.getLogger()
root.setLevel(logging.INFO)


class TestRefresh(unittest.TestCase):
    def setUp(self):
        super(TestRefresh, self).setUp()
        ensure_repo_exists(TMP_REPO_DIR)
        shutil.copyfile(os.path.join('tests/testdata/simple.yaml'), 
                        os.path.join(TMP_REPO_DIR, 'mysql_hook_test.yaml'))

    def test_refresh_simple(self):
        command_line.cli(['--repo', TMP_REPO_DIR, 'refresh', 'mysql_hook_test'])
