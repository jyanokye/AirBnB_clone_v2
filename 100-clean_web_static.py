#!/usr/bin/python3
"""full deployment to web servers"""
import os.path
from fabric.api import *
from datetime import datetime
env.hosts = ['54.157.191.136', '54.157.163.118']


def do_clean(number=0):
    """Deletes outdated archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
