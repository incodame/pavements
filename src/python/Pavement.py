#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:51:38 2022

@author: incodame
"""
from typing import NamedTuple
import array
import yaml
from Application import Application
from FileContainer import FileContainer

class Pavement(NamedTuple):
    name: str
    repository: str
    apps: array.array
    containers: array.array
    parameters: array.array
    connect: array.array 
    
    def loadFrom(self, file: str):
        yaml_fragment = ""
        with open(file) as f:
            try:
                yaml_fragment = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        for app in yaml_fragment['paragraph']['apps']:
            self.apps.append(Application(name=app['name'], 
                                         build=app.get('build', 'unknown'),
                                         repositories=app.get('repositories', []),
                                         modules=app.get('modules',[]),
                                         deployments=app.get('deployments',[])))
        for cont in yaml_fragment['paragraph']['graph']['file']:
            container = yaml_fragment['paragraph']['graph']['file'][cont]
            self.containers.append(FileContainer(name=cont, 
                                         type='file',
                                         loc=container.get('loc', ''),
                                         doc=container.get('doc', ''),
                                         params=container.get('params',[])))
    
    def toYaml(self):
        return """
        pavement:
            name: $name
        """

if __name__ == '__main__':
    p = Pavement('test', 'test', [], [], [], [])
    p.loadFrom('/Users/tanguyro/Incodame/paragraph/paragraph.yml')