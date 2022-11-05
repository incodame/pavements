#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:58:48 2022

@author: incodame
"""

from Container import Container

class ArchiveContainer(Container):
        
    def toYaml(self):
        return """
        archive:
            name: $name
        """