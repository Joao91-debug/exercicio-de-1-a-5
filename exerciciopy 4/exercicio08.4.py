import platform

def informacoes_do_sistema():
    sistema = platform.system()
    versao = platform.version()
    release = platform.release()

    print("Informações do Sistema:")
    print(f"Sistema Operacional: {sistema}")
    print(f"Versão: {versao}")
    print(f"Release: {release}")


informacoes_do_sistema()