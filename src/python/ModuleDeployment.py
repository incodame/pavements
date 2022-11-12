#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:42:31 2022

@author: incodame
"""

from typing import NamedTuple
import array

class ModuleDeployment(NamedTuple):
    name: str
    files: array.array
    archives: array.array
    
    def toYaml(self):
        return """
        TODO
        """