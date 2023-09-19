import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def obter_dados():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    dados = [nome, sobrenome, data_nascimento]
    return dados

def obter_tamanho_senha():
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    return tamanho

dados_usuario = obter_dados()
tamanho_senha = obter_tamanho_senha()
senha_gerada = gerar_senha(tamanho_senha)

print("Dados do usuário:", dados_usuario)
print("Senha gerada:", senha_gerada)