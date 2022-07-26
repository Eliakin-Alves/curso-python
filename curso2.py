nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))
print(f"O aluno {nome} matriculado no cuso de Phyton possui {idade} anos")
if(idade >= 18):
    print(f"{nome} esta apto a tirar a CNH")
else:
    print(f"{nome} esta inapto a tirar a CNH")
