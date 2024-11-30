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
from ParagraphContainer import ParagraphContainer
from FileContainer import FileContainer
from ArchiveContainer import ArchiveContainer
from Parameter import Parameter
from ApplicationDeployment import ApplicationDeployment
from ModuleDeployment import ModuleDeployment
from Tag import Tag

class Pavement(NamedTuple):
    name: str
    repository: str
    apps: list[Application]
    containers: list[ParagraphContainer]
    parameters: list[Parameter]
    deployments: list[ApplicationDeployment]
    connect: array.array
    tags: list[Tag]

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
            Pavement.check_yaml_consistency(root)
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
    
    @staticmethod
    def check_yaml_consistency(pavement):
        """Check for consistency of cross-references in the pavement definition"""
        try:
            # Navigate to the 'param' section in the YAML structure
            params = pavement['graph']['param']
            param_keys = params.keys()
            files = pavement['graph']['files']

            # Check each parameter sub param references
            for key, value in params.items():
                if 'params' in value:
                    Pavement.check_sub_param_list(key, value['params'], param_keys)

            # Check files sub param references
            for key, value in files.items():
                if 'params' in value:
                    Pavement.check_sub_param_list(key, value['params'], param_keys)

        except KeyError as e:
            print("Key error in YAML structure: {e}")

    @staticmethod
    def check_sub_param_list(key, sub_param_list, param_keys):
        for sub_param in sub_param_list:
            #  Extract the referenced param name (e.g. 'version' from 'param(version)')
            ref_param = Pavement.param_ref(sub_param)
            if ref_param not in param_keys:
                print(f"Param Reference error: '{ref_param}' referenced in '{key}' does not exist.")

    @staticmethod
    def param_ref(sub_param):
        sub_param_val: str = sub_param.get(list(sub_param.keys())[0])
        if "param(" in sub_param_val:
            return sub_param_val.split('(')[-1].strip(')')
        else:
            return list(sub_param.keys())[0]             

    def inherit_from(self, itags: list[Tag]):
        """loads content from the templates corresponding to the given tags"""
        for itag in itags:
            if itag not in self.tags:
                template_file = itag.get_template()
                if template_file is not None:
                    self.load_from(template_file)
                    self.tags.append(itag)
    
    @staticmethod
    def parse_param_loc_expr(loc_expr: str) -> tuple[str, str]:
        """parses a prolog term of the form: <type>(<expression>) """
        match = re.search(r"([^(]+)\(([^)]+)\)", loc_expr)
        return match.group(1), match.group(2)
    
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
    p.inherit_from([Tag(genre='framework', name='springboot', version='3.3')])
    p.inherit_from([Tag(genre='build', name='maven', version='')])
    print(p.to_yaml())
    