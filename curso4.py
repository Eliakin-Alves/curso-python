n = int(input("Qual a quantidade de alunos dessa turma? "))
total = 0 
for i in range(1, n+1):
    med = float(input(f"Digite a media do {i}º aluno: "))
    total = total + med
med_tur = total/n
print(f"A media da turma foi {med_tur}")
