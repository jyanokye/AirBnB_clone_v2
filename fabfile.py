#!/usr/bin/python3
"""deploy web_static folder to my servers"""
from datetime import datetime
from fabric.api import *
import os.path


env.user = 'ubuntu'
env.hosts = ['54.157.191.136', '54.157.163.118']


def do_deploy(archive_path):
    """deploy the tgz item to my web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        symp = '/data/web_static/current'
        put(archive_path, '/tmp/')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} {}'.format(path, symp))
        return True
    except Exception:
        return False
