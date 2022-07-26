nome = input("Qual o seu nome ")
nota1 = float(input("Digite a sua primeira nota "))
nota2 = float(input("Digite a sua primeira nota "))
media = (nota1+nota2)/2
if(media>=7):
    print(f"{nome} você está aprovado")
elif(media>=4):
    print(f"{nome} você precisa fazer a prova final")
else:
    print(f"{nome} você está reprovado")
