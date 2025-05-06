import random
import string

def gerar_senha():

    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(10))

    return senha

senha_gerada = gerar_senha()
print(f'Senha gerada: {senha_gerada}')