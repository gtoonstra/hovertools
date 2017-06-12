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
import sys
import click
import logging
from hovertools.actions import register_action
from hovertools.actions import refresh_action
from hovertools.utils import ensure_repo_exists


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
root = logging.getLogger()
root.setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class ExpandedPath(click.Path):
    def convert(self, value, *args, **kwargs):
        value = os.path.expanduser(value)
        return super(ExpandedPath, self).convert(value, *args, **kwargs)


@click.group()
@click.option('-r', 
              '--repo', 
              type=ExpandedPath(exists=False,
                                file_okay=False,
                                dir_okay=True,
                                writable=True,
                                readable=True,
                                resolve_path=True),
              default='~/.hovertools')
@click.pass_context
def cli(ctx, repo):
    if ctx.obj is None:
        ctx.obj = {}
    ensure_repo_exists(repo)
    ctx.obj['repo'] = repo


@click.command()
@click.argument('filename')
@click.pass_context
def register(ctx, filename):
    logger.info('Registering a new docker instance configuration')
    register_action.do_register(ctx, filename)


@click.command()
@click.argument('name')
@click.pass_context
def refresh(ctx, name):
    logger.info('Refreshing a docker instance by name')
    refresh_action.do_refresh(ctx, name)


cli.add_command(register)
cli.add_command(refresh)


if __name__ == '__main__':
    cli(obj={})
