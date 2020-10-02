#! /usr/bin/env python3
import os
import docker
import shutil
import subprocess
from os import path
from jinja2 import Template

# Setup Script
# 1. Creates a volume using the docker python api
# 2. Copies files / creates directories within the volume
# 3. generates a docker-compose.yml file from docker-compose.yml.jinja2 via jinja2
# 4. runs "docker-compose up -d" which uses bind mounts to map the files / directories into the container
# Note since there's no way to create files / directories remotely via docker, this script needs to be run on the local host


class DockerRun(object):
    '''Docker Setup Script'''

    def __init__(self):
        '''Default docker host connection'''
        self.DockerHost = 'unix:///var/run/docker.sock'
        '''Path to docker-compose executable'''
        self.DockerCompose = 'docker-compose'
        '''Data volume'''
        self.DockerVolume = 'devel_webproxymgr'
        '''Project / stack name'''
        self.DockerProjectName='devel'
        '''Working Directory'''
        self.WorkDir = '.'

    def main(self):

        # Setup the volume
        volume_dir = self.create_volume()
        cfgfile, datadir, encdir = self.copy_volume_files(volume_dir)

        # Parse docker-compose.yml.jinja2 into docker-compose.yml
        print('Generating docker-compose.yml')
        with open('docker-compose.yml.jinja2') as tmpl_file:
            template = Template(tmpl_file.read())
        tmpl_str = template.render(config_file=cfgfile, letsencrypt_dir=encdir, data_dir=datadir, vol_name=self.DockerVolume)
        with open('docker-compose.yml', 'w') as out_file:
            out_file.write(tmpl_str)

        # Launch docker-compose
        print("Running " + self.DockerCompose)
        proc_out, proc_err = self.run_compose()

    def create_volume(self):
        '''Make sure the volume exists if it doesn't already'''
        print("Setting up volume")
        client = docker.DockerClient(base_url=self.DockerHost)
        volume = client.volumes.create(name=self.DockerVolume)
        volume_dir = volume.attrs['Mountpoint']
        return volume_dir

    def copy_volume_files(self, volume_dir):
        '''Copy files / directories into the volume'''
        print("Copying files to volume")

        cfgfile=path.join(volume_dir, 'config.json')
        shutil.copy2('config.json', cfgfile)

        datadir=path.join(volume_dir, 'data')
        if not path.exists(datadir):
            os.mkdir(datadir)

        encdir=path.join(volume_dir, 'letsencrypt')
        if not path.exists(encdir):
            os.mkdir(encdir)

        return cfgfile, datadir, encdir

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
