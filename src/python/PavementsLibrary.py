#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:41:46 2022

@author: tanguyro
"""
import os

class PavementsLibrary:
    
    def find_template(genre: str, name: str, ver: str) -> str:
        libdir = os.getenv('PAVEMENTS_LIBRARY')
        if libdir is None:
            return None
        
        if os.path.isdir(libdir):
            return f"{libdir}/{genre}/{name}.yml"
        else:
            return None
        
if __name__ == '__main__':
    print(PavementsLibrary.find_template("framework", "springboot", None))
    