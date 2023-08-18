'''
Crie uma classe Aluno que terá como atributos a matrícula, o nome, o curso e uma lista de notas. 
Para realizar o cadastro do aluno, deve-se verificar se o curso está cadastrado em uma lista pré-definida 
como todos os cursos da escola.
Você também deve criar os métodos de cadastrar nota, calcular média e mostrar resultado.
'''

class Aluno:
    
    def __init__(self, matricula, nome, curso):
        lista_cursos = ['Adm', 'Direito', 'Psico']
        if curso in lista_cursos:
            self.matricula = matricula
            self.nome = nome
            self.curso = curso 
            self.notas = []
        else:
            print('Não foi possível realizar a matrícula, pois o curso escolhido não consta nas opções ofertadas')
            self.matricula = 0
            self.nome = 0
            self.curso = 0 
            self.notas = []

    def cadastrar_nota(self):
        while True:
            nota = input('Digite uma nota do aluno: ')            
            if nota == 'x':
                break
            self.notas.append(float(nota))     

    def media(self):
        soma = contador = 0
        for i in self.notas:
            soma += i
            contador +=1 
        print(f'Média do aluno: [ {soma / contador} ]')
    
    def get_info(self):
        print(f'Informações do aluno: mat.: [ {self.matricula} ], nome: [ {self.nome} ], curso: [ {self.curso} ], notas: [ {self.notas} ]')

a1 = Aluno(1, 'Ana', 'Adm')
a1.get_info()
a1.cadastrar_nota()
print(a1.notas)
a1.media()



