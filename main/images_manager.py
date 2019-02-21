#venv/bin/python
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
        # image_name = 'sunnywalden/prometheus-webhook-dingding'
        # image_tag = 'v0.3.8'
        # image_name = 'sunnywalden/shuangse-lottery'
        # image_tag = 'v0.5.4'
        # image_name = 'sunnywalden/nodes_exporters_discovery'
        # image_tag = 'v0.1'

    def logs_image(self, container_id):
        """
            Get docker logs
        """
        # cont_id = '073c0e511b19'
        container = self.docker_client.containers.get(container_id)
        logs = container.logs().decode('utf-8')
        return logs

    def get_images(self):
        """
            Get image list
        """
        return self.docker_client.images.list()

    def search_images(self):
        """
            Search images in docker registry
        """
        return self.docker_client.images.search('sunnywalden/')

    def get_image(self, image_name):
        """
            Get image list
        """
        return self.docker_client.images.get(image_name)

    def pull_image(self, image_name, image_tag='latest'):
        """
            Pull image from registry
        """
        return self.docker_client.images.pull(image_name, tag=image_tag)

    def push_image(self, image_name, image_tag='latest'):
        """
            Push image to registry
        """
        return self.docker_client.images.push(repository=image_name, tag=image_tag)

    def tag_image(self, image_name, image_tag, tag='latest'):
        """
            Tag image
        """
        docker_tagger = docker.client.APIClient()
        return docker_tagger.tag(image=image_name + ':' + image_tag, repository=image_name, tag=tag)

    def remove_image(self, image_name):
        return self.docker_client.images.remove(image_name)
