#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:39:18 2022

@author: incodame
"""

from typing import NamedTuple

class Parameter(NamedTuple):
    name: str
    type: str
    loc: str
    doc: str
    params: list
        
    def toYaml(self):
        return """
        parameter:
            name: $name
        """