#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:51:38 2022

@author: incodame
"""
from typing import NamedTuple
import array
import yaml
import re
from Application import Application
from FileContainer import FileContainer
from ArchiveContainer import ArchiveContainer
from Parameter import Parameter
from ApplicationDeployment import ApplicationDeployment
from ModuleDeployment import ModuleDeployment
from Tag import Tag

class Pavement(NamedTuple):
    name: str
    repository: str
    apps: array.array
    containers: array.array
    parameters: array.array
    deployments: array.array
    connect: array.array
    tags: array.array

    def load_from(self, file: str):
        """enriches the internal collections with the yaml source content"""
        yaml_fragment = ""
        with open(file) as f:
            try:
                yaml_fragment = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        root = yaml_fragment.get('pavement', None)
        if root is None:
            root = yaml_fragment.get('paragraph', None)
        if root is not None:
            for app in root['apps']:
                self.apps.append(Application(name=app['name'], 
                                        tags=app.get('tags', []),
                                        repositories=app.get('repositories', []),
                                        modules=app.get('modules',[]),
                                        deployments=app.get('deployments',[])))
            for cont in root['graph'].get('file', []):
                container = root['graph']['file'][cont]
                self.containers.append(FileContainer(name=cont, 
                                        type='file',
                                        loc=container.get('loc', ''),
                                        doc=container.get('doc', ''),
                                        params=container.get('params',[])))        
            for cont in root['graph'].get('archive', []):
                container = root['graph']['archive'][cont]
                self.containers.append(ArchiveContainer(name=cont, 
                                        type='archive',
                                        loc=container.get('loc', ''),
                                        doc=container.get('doc', ''),
                                        params=container.get('params',[])))
            for param in root['graph'].get('param', []):
                parameter = root['graph']['param'][param]
                self.parameters.append(Parameter(name=param, 
                                        type=self.parameter_type(parameter.get('loc', '')),
                                        loc=parameter.get('loc', ''),
                                        doc=parameter.get('doc', ''),
                                        params=parameter.get('params',[])))
            for depl in root['graph'].get('deployment', []):
                deployment = root['graph']['deployment'][depl]
                app_deployment = ApplicationDeployment(name=depl, 
                                        modules=[], 
                                        location=None)
                for modu in deployment:
                    module = deployment[modu]
                    app_deployment.modules.append(ModuleDeployment(name=modu,
                                        files=module.get('files', []),
                                        archives=module.get('archives', [])))
                self.deployments.append(app_deployment)
            # todo - read tag version
            pv_tag_names = [ list(tg)[0] for tg in root['tags']]
            pavement_tags = [ Tag(genre=tn, name=root['tags'][indx][tn], version='') for indx, tn in enumerate(pv_tag_names)]
            self.inherit_from(pavement_tags)
    
    def inherit_from(self, itags: array.array):
        """loads content from the templates corresponding to the given tags"""
        for itag in itags:
            if itag not in self.tags:
                template_file = itag.get_template()
                if template_file is not None:
                    self.load_from(template_file)
                    self.tags.append(itag)
    
    @staticmethod
    def parse_param_loc_expr(loc_expr: str) -> (str, str):
        """parses a prolog term of the form: <type>(<expression>) """
        match = re.search(r"([^(]+)\(([^)]+)\)", loc_expr)
        return (match.group(1), match.group(2))
    
    @staticmethod
    def parameter_type(loc_expr: str) -> str:
        """returns the type of a parameter based on the loc expression"""
        return Pavement.parse_param_loc_expr(loc_expr)[0]
    
    def to_yaml(self):
        return """
        pavement:
            name: $name
        """

if __name__ == '__main__':
    p = Pavement('test', 'test', [], [], [], [], [], [])
    p.load_from('/Users/tanguyro/Incodame/paragraph/paragraph.yml')
    p.inherit_from([Tag(genre='framework', name='springboot', version='2.3.0')])
    p.inherit_from([Tag(genre='build', name='maven', version='')])
    