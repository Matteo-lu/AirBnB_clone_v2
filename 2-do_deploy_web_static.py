""" script that sets up your web servers for the deployment of web_static """

from fabric.api import env, run, put

env.hosts = ['35.229.127.214', '3.89.225.59']


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
    from fabric.context_managers import cd

    file_name = str(archive_path.replace('versions/', ''))
    name = file_name.replace('.tgz', '')
    path_deploy = "/data/web_static/releases/"
    web_st = "/web_static/"

    with cd("/tmp"):
        if put(archive_path, file_name).failed:
            return (False)
        elif run("mkdir -p path_deploy%s" % (name)).failed:
            return (False)
        elif run('tar -xzf %s -C path_deploy%s' % (file_name, name)).failed:
            return (False)
        elif run('mv path_deploy%sweb_st* path_deploy%s/' % (name, name)):
            return(False)
        elif run('rm -rf path_deploy%s/web_static' % (name)).failed:
            return (False)
    with cd("/data/web_static"):
        if run('rm -rf current').failed:
            return (False)
        elif run('ln -s path_deploy%s path_deploycurrent' % (name)).failed:
            return (False)
    return (True)
