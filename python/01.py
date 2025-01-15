import docker

# Inicializa o cliente Docker usando as configurações do ambiente
client = docker.from_env()

# Executa o container 'hello-world' e exibe o resultado
output = client.containers.run("hello-world")
print(output.decode())  # Decodifica o byte output para string