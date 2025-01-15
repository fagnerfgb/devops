import docker

# Inicializa o cliente Docker usando as configurações do ambiente
client = docker.from_env()

# Substitua pelo ID do container desejado
container_id = "d52ebbd73bcd93fa667f2626136f0d065a53d4d08e7b023a5b49b25583841405"

# Obtém o container específico pelo ID
container = client.containers.get(container_id)

# Remove o container, forçando a remoção mesmo que ele esteja em execução
container.remove(force=True)

print(f"Container {container_id} removido com sucesso.")