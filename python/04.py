import docker

client = docker.from_env()

container = client.containers.get("d52ebbd73bcd93fa667f2626136f0d065a53d4d08e7b023a5b49b25583841405")
print(f'{container.id} - {container.image.tags} - {container.name}')