#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:58:48 2022

@author: incodame
"""

from typing import NamedTuple
import array

class Container(NamedTuple):
    name: str
    type: str
    loc: str
    doc: str
    params: array.array
        
    def toYaml(self):
        return """
        container:
            name: $name
        """