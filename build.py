from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pomo"
default_task = "publish"
version = '0.10'


@init
def set_properties(project):
    project.depends_on('pygame')
    project.depends_on('docopt')
    project.depends_on('pyyaml')
    with open('src/main/python/pomo/__init__.py', 'w') as f:
        f.write('version = {}'.format(version))
