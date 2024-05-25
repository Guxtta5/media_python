# Declaração de variaveis 
# Números inteiros = int / Números reais = float 
# Caracteres = str / verdadeiro ou falso = bool
nota1 : float
nota2 : float
nota3 : float
nota4 : float
media : float
aluno : str
numerosala : int
professor : str
materia : str
quantidade : int
contador : int

# Pegando informações iniciais
professor = str(input("Digite seu nome por favor: "))
print("Olá professor: ",professor)

materia = str(input("Qual é a materia que leciona? "))
print("Certo professor: ",professor," de ",materia )

numerosala = int(input("Qual é o número da sala que irá calcular as notas ? "))

# Adicionando a entrada da variavel decisão
quantidade = int(input("Digite o número de alunos que ira calcular a média: "))


# Laço de repetição (while) para qualcular media de mais de um aluno 
for contador in range(quantidade) :

    # Pegando informações do aluno
     
    aluno = str(input("Qual é o nome do aluno? "))
    print("Certo professor: ",professor,", o nome do aluno que será avaliado é: ",aluno)


    # Recebendo os valores de nota1 e nota2, variaveis de entrada 
    nota1 = float(input("Digite a nota do primeiro bimestre do aluno: "))
    nota2 = float(input("Digite a nota do segundo bimestre do aluno: "))
    nota3 = float(input("Digite a nota do terceiro bimestre do aluno: "))
    nota4 = float(input("Digite a nota do quarto bimestre do aluno: "))

    # Fazendo o processamento das notas
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Exiboindo o resultado
    print("A média final do aluno em " ,materia," e de: ",media)

    # laço condicional simples (if, elif, else)
    if media < 5 : 
        print("O aluno: ",aluno," reprovou de ano, QUE PENA... ")
    elif media >= 5 and media < 7 : 
        print("O aluno: ",aluno," esta de recuperação, e precisara realizar uma prova ")
    else : 
        print("O aluno: ",aluno," passou de ano, PARABÉNS")

    print(contador,"°",aluno)


print("OBRIGADO, Volte sempre!!")