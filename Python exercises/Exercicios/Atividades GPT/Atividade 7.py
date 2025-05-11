import re

def validar_senha(senha):
    if len(senha) < 8:
        print("Senha fraca: menos de 8 caracteres.")
        return False
    elif not re.search(r"[A-Z]", senha):
        print("Senha fraca: precisa de uma letra maiúscula.")
        return False
    elif not re.search(r"[0-9]", senha):
        print("Senha fraca: precisa de um número.")
        return False
    else:
        print("Senha forte! Parabéns.")
        return True