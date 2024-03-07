'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''

texto = "Olá, mundo!"

texto_invertido = ""

for i in range(len(texto)-1, -1, -1):
  texto_invertido += texto[i]

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")