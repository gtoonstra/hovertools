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
from hovertools.managers.docker_manager import DockerManager

logger = logging.getLogger(__name__)


def do_refresh(ctx, name):
    """"
    Refreshes a docker instance by name
    """
    yaml_doc = None

    try:
        repo_dir = ctx.obj['repo']
        filename = os.path.join(repo_dir, name+'.yaml')
        with open(filename, 'r') as fin:
            yaml_doc = yaml.safe_load(fin)
    except yaml.YAMLError as e:
        raise Exception("Error in configuration file: {0}".format(e))

    docker_manager = DockerManager(image_name=yaml_doc['image'], 
                                   container_name=yaml_doc['name'],
                                   environment=yaml_doc['environment'],
                                   ports=yaml_doc['ports'])
    logger.info("Refreshing")
    docker_manager.refresh()
