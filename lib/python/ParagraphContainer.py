#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:58:48 2022

@author: incodame
"""

from typing import NamedTuple
from Parameter import Parameter

class ParagraphContainer(NamedTuple):
    name: str
    type: str
    loc: str
    doc: str
    params: list[Parameter]
        
    def toYaml(self):
        return """
        container:
            name: $name
        """