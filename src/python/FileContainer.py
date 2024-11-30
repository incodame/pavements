#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:58:48 2022

@author: incodame
"""

from ParagraphContainer import ParagraphContainer

class FileContainer(ParagraphContainer):
        
    def toYaml(self):
        return """
        file:
            name: $name
        """