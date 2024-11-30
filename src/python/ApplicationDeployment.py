#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:42:31 2022

@author: incodame
"""

from typing import NamedTuple
from ModuleDeployment import ModuleDeployment

class ApplicationDeployment(NamedTuple):
    name: str
    modules: list[ModuleDeployment]
    location: str
    
    def toYaml(self):
        return """
        deployment:
            name: $name
        """