# venv/bin/python
# -*- coding:utf-8 -*-

from logbook import Logger
from logbook import TimedRotatingFileHandler
import docker
import os


class ImagesManager(object):
    def __init__(self):
        handler = TimedRotatingFileHandler('../logs/images_manager.log')
        handler.push_application()
        self.logger = Logger(name='Docker Images Manage Api', level=11)

        os.environ['DOCKER_API_VERSION'] = 1.39
        self.logger.debug(os.environ.get('DOCKER_API_VERSION'))
        DOCKER_API_VERSION = 1.39
        self.docker_client = docker.from_env()

    def run_container(self, image_name, cont_name, command, detach=True, cont_ports={}):
        return self.docker_client.containers.run(image=image_name, command=command, name=cont_name, detach=detach, \
                                                 ports=cont_ports)

    def commit_container(self, container, commits):
        container.wait()
        return container.commit(commits)

    def get_container(self, cont_id):
        return self.docker_client.containers.get(cont_id)

    def list_container(self, **kwargs):
        return self.docker_client.containers.list(kwargs)

    def remove_container(self, cont_id):
        return docker.client.APIClient.remove_container(cont_id)

