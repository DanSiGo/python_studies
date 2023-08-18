""" Implemente uma classe Aluno, que deve ter os seguintes atributos: 
nome, curso, tempoSemDormir (em horas).

Essa classe deverá ter os seguintes métodos:

estudar (que recebe como parâmetro a qtd de horas
de estudo e acrescenta tempoSemDormir )

Dormir (que recebe como parâmetro a qtd de horas de
sono e reduz tempoSemDormir )

Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir.
Ao final imprima quanto tempo o aluno está sem dormir """

class Aluno:
    def __init__(self, n, c, t):
        self.nome = n
        self.curso = c
        self.tempo_sem_dormir = t

    def estudar(self, horas):
        self.tempo_sem_dormir += horas

    def dormir(self, sono):              
        self.tempo_sem_dormir -= sono
        self.tempo_sem_dormir *= -1
        
'''
teste_aluno = Aluno('a', 'adm', 5)

teste_aluno.estudar(4)
print(f'O aluno está há {teste_aluno.tempo_sem_dormir} horas sem dormir')

teste_aluno.dormir(8)
print(f'O aluno dormiu por 8 horas e agora tem {teste_aluno.tempo_sem_dormir} hora de saldo de sono')
'''