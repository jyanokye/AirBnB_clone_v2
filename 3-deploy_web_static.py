#!/usr/bin/python3
"""full deployment to web servers"""
import os.path
from fabric.api import *
from datetime import datetime
env.hosts = ['54.157.191.136', '54.157.163.118']


def do_pack():
    """
    making an archive on web_static folder
    """
    try:
        time = datetime.now()
        archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(archive))
        return ("versions/{}".format(archive))
    except Exception:
        return None


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


def deploy():
    """calls two functions to fully deploy
    the web_static folder
    """
    try:
        archive_name = do_pack()
        item = do_deploy(archive_name)
        return item
    except Exception:
        return False
