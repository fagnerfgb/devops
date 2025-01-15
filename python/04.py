import docker

# Inicializa o cliente Docker usando as configurações do ambiente
client = docker.from_env()

# Substitua o ID pelo ID real do container que deseja inspecionar
container_id = "d52ebbd73bcd93fa667f2626136f0d065a53d4d08e7b023a5b49b25583841405"

# Obtém o container específico pelo ID
container = client.containers.get(container_id)

# Imprime as informações do container
print(f'{container.id} - {container.image.tags} - {container.name}')