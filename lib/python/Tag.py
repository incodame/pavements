#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:51:22 2022

@author: incodame
"""

from typing import NamedTuple
from PavementsLibrary import PavementsLibrary

class Tag(NamedTuple):
    genre: str
    name: str
    version: str
    
    def __eq__(self, other):
        return (
            isinstance(other, Tag)
            and self.name == other.name
            and self.genre == other.genre
            and self.version == other.version
        )
    
    def get_template(self) -> str:
        return PavementsLibrary.find_template(self.genre, self.name, self.version)
    
if __name__ == '__main__':
    assert Tag(genre='build', name='maven', version='3.6') == Tag(genre='build', name='maven', version='3.6')