import docker

# Inicializa o cliente Docker usando as configurações do ambiente
client = docker.from_env()

# Obtém a lista de todos os containers (ativos e inativos)
lista_containers = client.containers.list(all=True)

# Itera sobre a lista e imprime as informações dos containers
for item in lista_containers:
    print(f'{item.id} - {item.image.tags} - {item.name}')