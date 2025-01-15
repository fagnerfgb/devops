import docker

client = docker.from_env()

lista_containers = client.containers.list(all=True)

for item in lista_containers:
	print(f'{item.id} - {item.image.tags} - {item.name}')