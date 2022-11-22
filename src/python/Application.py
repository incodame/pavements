#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:51:22 2022

@author: incodame
"""

from typing import NamedTuple
import array

class Application(NamedTuple):
    name: str
    repositories: array.array
    modules: array.array
    deployments: array.array
    tags: array.array
    
    def toYaml(self):
        return """
        application:
            name: $name
        """