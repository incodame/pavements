#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:42:31 2022

@author: incodame
"""

from typing import NamedTuple
from FileContainer import FileContainer
from ArchiveContainer import ArchiveContainer


class ModuleDeployment(NamedTuple):
    name: str
    files: list[FileContainer]
    archives: list[ArchiveContainer]
    
    def toYaml(self):
        return """
        TODO
        """