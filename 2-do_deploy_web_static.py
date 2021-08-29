#!/usr/bin/python3
""" deploying the web_static work using Fabric (for Python3)."""

from fabric.api import env
from fabric.context_managers import cd
from fabric.api import run, put, local, settings
from os.path import isfile


env.hosts = ['35.229.127.214', '3.89.225.59']


def do_pack():
    """ script that generates a .tgz archive from the
    contents of the web_static folder of your AirBnB
    Clone repo, using the function do_pack
    """
    from fabric.api import local
    from datetime import datetime
    from fabric.context_managers import cd
    import os.path

    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    file_name = 'web_static_' + dt_string
    source_dir = 'web_static'

    if not os.path.exists('versions'):
        local("mkdir -p versions")
    local("tar -zcvf versions/%s.tgz --absolute-names %s" %
          (file_name, source_dir))
    path_file = 'versions' + '/' + file_name + '.tgz'

    if os.path.exists(path_file):
        return(path_file)
    else:
        return(None)


def do_deploy(archive_path):
    """script that distributes an archive to your web servers,
    using the function do_deploy
    """
    file_name = str(archive_path.replace('versions/', ''))

    just_name = file_name.replace('.tgz', '')
    path_releases = "/data/web_static/releases"
    path_current = "/data/web_static/current"
    full_path = path_releases + "/" + just_name
    wb_st = "/web_static"

    if not isfile(archive_path):
        return (False)

    try:
        put(archive_path, "/tmp/" + file_name)
        run("mkdir -p " + path_releases + "/" + just_name + "/")
        run("tar -xzf /tmp/" + file_name + " -C " + full_path + "/")
        run("rm /tmp/" + file_name)
        run("mv " + full_path + wb_st + "/* " + full_path + "/")
        run("rm -rf " + full_path + wb_st)
        run("rm -rf /data/web_static/current")
        run("ln -s " + full_path + "/ /data/web_static/current")
        return(True)
    except:
        return (False)
