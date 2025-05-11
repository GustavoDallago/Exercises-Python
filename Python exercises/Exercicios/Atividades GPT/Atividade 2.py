import re

msg = "Olá!! Meu número é 123-456-7890... Me ligue!!!"

refeito = re.sub(r"[^\w\s]", "", msg)

print(refeito)