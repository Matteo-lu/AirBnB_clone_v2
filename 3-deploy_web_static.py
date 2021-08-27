#!/usr/bin/python3
""" script that sets up your web servers for the deployment of web_static """

from fabric.api import env, run, put
from os.path import isfile

env.hosts = ['35.243.253.93', '3.81.226.200']


def do_pack():
    """ script that sets up your web servers for the
    deployment of web_static """

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
