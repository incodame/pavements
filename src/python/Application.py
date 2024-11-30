#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:51:22 2022

@author: incodame
"""

from typing import NamedTuple
from Tag import Tag
from ApplicationDeployment import ApplicationDeployment
from ModuleDeployment import ModuleDeployment

class Application(NamedTuple):
    name: str
    repositories: list[str]
    modules: list[ModuleDeployment]
    deployments: list[ApplicationDeployment]
    tags: list[Tag]
    
    def toYaml(self):
        return """
        application:
            name: $name
        """