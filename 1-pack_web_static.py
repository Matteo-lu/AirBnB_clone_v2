#!/usr/bin/python3
""" script that sets up your web servers for the deployment of web_static """


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
