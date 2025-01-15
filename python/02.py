import docker

# Inicializa o cliente Docker usando as configurações do ambiente
client = docker.from_env()

# Executa o container 'nginx', desanexado e mapeando a porta 80 do container para a porta 8080 do host
container = client.containers.run(
    "nginx", 
    detach=True,  # Executa o container em segundo plano
    ports={"80/tcp": ("0.0.0.0", 8080)}  # Mapeia a porta do container para o host
)

# Exibe o ID do container criado
print(f"Container ID: {container.id}")