# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import subprocess

from .exceptions import ProgramError


def _subprocess_copy(text, args_list):
    p = subprocess.Popen(args_list, stdin=subprocess.PIPE, close_fds=True)
    p.communicate(input=text.encode('utf-8'))


def copy(text):
    """
    Copy text to OS clipboard.
    """

    if sys.platform == 'darwin':
        copy_osx(text)
    else:
        # For Linux, BSD, cygwin, etc.
        copy_linux(text)


def copy_osx(text):
    _subprocess_copy(text, ['pbcopy', 'w'])


def copy_linux(text):

    def get_command_name():
        # Checks for the installation of wl-copy, or xsel or xclip
        # depending if WAYLAND_DISPLAY is set
        if 'WAYLAND_DISPLAY' in os.environ:
            cmds = ['wl-copy']
        else:
            cmds = ['xsel', 'xclip']
        for cmd in cmds:
            cmd_exists = subprocess.call(
                ['which', cmd],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
            if cmd_exists:
                return cmd
        return None

    cmd_args = {
        'xsel': ['xsel', '-b', '-i'],
        'xclip': ['xclip', '-selection', 'c'],
        'wl-copy': ['wl-copy']}
    cmd_name = get_command_name()

    if cmd_name is None:
        raise ProgramError("External copy application not found")

    _subprocess_copy(text, cmd_args.get(cmd_name))
