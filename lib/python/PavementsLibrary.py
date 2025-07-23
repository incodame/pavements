#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:41:46 2022

@author: tanguyro
"""
import os

class PavementsLibrary:
    env_warning: bool = False
    
    def find_template(genre: str, name: str, ver: str) -> str:
        libdir = os.getenv('PAVEMENTS_LIBRARY')
        if libdir is None:
            if not PavementsLibrary.env_warning:
                print ("PAVEMENTS_LIBRARY environment variable is not set.")
                PavementsLibrary.env_warning = True
            return None
        
        if os.path.isdir(libdir):
            return f"{libdir}/{genre}/{name}.yml"
        else:
            print(f"Could not find template {name} of genre {genre} in {libdir}.")
            return None
        
if __name__ == '__main__':
    # Dynamically set PAVEMENTS_LIBRARY based on the project root
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))  # Go up 3 levels
    pavements_library_path = os.path.join(project_root, "library")
    os.environ["PAVEMENTS_LIBRARY"] = pavements_library_path
    # Test the PavementsLibrary functionality
    print(PavementsLibrary.find_template("framework", "springboot", None))
    