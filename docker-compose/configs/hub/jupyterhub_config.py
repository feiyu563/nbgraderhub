import os

c = get_config()

image = 'nbhub/student'
network = 'nbhub_network'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = image
c.DockerSpawner.extra_create_kwargs.update({'command': 'start-singleuser.sh'})
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network
c.DockerSpawner.extra_host_config = {'network_mode': network}

c.DockerSpawner.notebook_dir = '/home/jovyan'
c.DockerSpawner.volumes = {
        'nbgrader_exchange_inbound_{username}': '/exchange/course/inbound', 
        'nbgrader_work_{username}': '/home/jovyan',
        'nbgrader_exchange_outbound': dict(
            bind='/exchange/course/outbound',
            mode='ro'
            )
        }
c.DockerSpawner.remove_containers = True

c.JupyterHub.hub_ip = 'nbhub_hub'
c.JupyterHub.hub_port = 8080
c.JupyterHub.port = 8000

from jupyterhub.auth import Authenticator
class MyAuthenticator(Authenticator):
    async def authenticate(self, handler, data):
        name = data['username']
        password = data['password']

        if name in ['albert.einstein', 'jack.bauer']:
            if password == 'jjj':
                return dict(name = name)

        return None

c.JupyterHub.authenticator_class = MyAuthenticator
c.JupyterHub.base_url = '/course'
