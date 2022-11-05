#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:42:31 2022

@author: incodame
"""

from typing import NamedTuple
import array

class ApplicationDeployment(NamedTuple):
    name: str
    modules: array.array
    location: str
    
    def toYaml(self):
        return """
        deployment:
            name: $name
        """