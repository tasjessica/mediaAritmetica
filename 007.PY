#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print("Sua média é {}.".format(media))

#se nao usassemos parenteses, ele faria primeiro a divisão e o programa rodaria, mas dando resultados errados.