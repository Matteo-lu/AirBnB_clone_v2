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
        (path_file)
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


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function do_deploy

    Args:
        archive_path ([file]): file at the path

    Returns:
        [bool]: True or False
    """
    if not isfile(archive_path):
        return (False)
    try:
        with cd("/tmp"):
            put(archive_path, file_name)
            run("mkdir -p %s%s" % (pt_deploy, name))
            run('tar -xzf %s -C %s%s' % (file_name, pt_deploy, name))
            run('mv %s%s%s* %s%s/' % (pt_deploy, name, wb_st, pt_deploy, name))
            run('rm -rf %s%s/web_static' % (pt_deploy, name))
        with cd("/data/web_static"):
            run('rm -rf current')
            run('ln -s %s%s %scurrent' % (pt_deploy, name, pt_deploy))
        return (True)
    except:
        return (False)


def deploy():
    """ script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy"""

    file_path = do_pack()
    if file_path is None:
        return (False)

    deploy_return = do_deploy(file_path)
    return (deploy_return)
