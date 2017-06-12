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

import os
import yaml
import logging


logger = logging.getLogger(__name__)


def do_register(ctx, filename):
    """"
    Registers a new yaml file.
    """
    try:
        repo_dir = ctx.obj['repo']
        stripped_file_name = os.path.basename(filename)
        new_file_path = os.path.join(repo_dir, stripped_file_name)
        with open(filename, 'r') as fin:
            document = yaml.safe_load(fin)
            with open(new_file_path, 'w') as fout:
                yaml.dump(document, fout)
    except yaml.YAMLError as exc:
        print("Error in configuration file: {0}".format(e))
