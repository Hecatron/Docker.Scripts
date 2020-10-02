#! /usr/bin/env python3
import os
import docker
import shutil
import subprocess
from os import path
from jinja2 import Template

# Setup Script

class DockerRun(object):
    '''Docker Setup Script'''

    def __init__(self):
        '''Default docker host connection'''
        self.DockerHost = 'unix:///var/run/docker-prod.sock'
        '''Path to docker-compose executable'''
        self.DockerCompose = 'docker-compose'
        '''Project / stack name'''
        self.DockerProjectName='live'
        '''Working Directory'''
        self.WorkDir = '.'

    def main(self):
        # Launch docker-compose
        print("Running " + self.DockerCompose)
        proc_out, proc_err = self.run_compose()

    def run_compose(self):
        '''Run docker-compose up -d'''
        if not shutil.which(self.DockerCompose):
            raise RuntimeError("The '" + self.DockerCompose + "' command was not found. Make sure you have " + self.DockerCompose + " installed")
        cmdarray = [self.DockerCompose]
        if self.DockerHost is not None:
            cmdarray += ['-H ' + self.DockerHost]
        cmdarray += ['--project-name=' + self.DockerProjectName, 'up', '-d']
        proc = subprocess.Popen(cmdarray, cwd=self.WorkDir, universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError('Failure to run command\n')
        return proc_out, proc_err

if __name__ == "__main__":
    DockerRun().main()
