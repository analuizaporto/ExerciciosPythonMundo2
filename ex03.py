# Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem final de acordo com a média atingida:
# Média abaixo de 5 → Reprovado
# Média entre 5 e 6.9 → Recuperação
# Média 7 ou superior → Aprovado

print('Vamos calcular a média das suas notas na sua prova de  Matemática e saberemos se você foi aprovado!')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabéns! Sua média é {:.1f} e você está APROVADO!'.format(media))
elif 5< media <6.9:
    print('Sua média é {:.1f} e você está de Recuperação! '.format(media))
else:
    print('Sua média é {:.1f} e você está Reprovado. '.format(media))
