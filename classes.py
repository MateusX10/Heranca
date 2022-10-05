class Profissional:
    def __init__(self, nome, idade, area, salario):
        self.nome = nome
        self.idade = idade
        self.area = area
        self.salario = salario
        self.nomeprofissional = self.__class__.__name__

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_valor):
        
        self._nome = novo_valor.title() # Joga todas as primeiras letras do nome da pessoa para maiúsculo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, novo_valor):
        if isinstance(novo_valor, str):
            try:
                novo_valor = int(novo_valor)
            except:
                if isinstance(novo_valor, float):
                    novo_valor = float(novo_valor)
                else:
                    novo_valor = 20

        if isinstance(novo_valor, float): # A idade está em ponto flutuante
            if "." in str(novo_valor): # 
                novo_valor = str(novo_valor)
                novo_valor = novo_valor.split(".")[0] 
        self._idade = novo_valor

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, nova_area):
        if isinstance(nova_area, int) or isinstance(nova_area, float):
            nova_area = "back-end"

        self._area = nova_area

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):

        if (isinstance(novo_salario, str)) or (isinstance(novo_salario, int)):
            try:
                novo_salario = float(novo_salario)
            except:
                if "R$" in str(novo_salario): # Tirando o R$ do salário e convertendo o salário para ponto flutuante
                    novo_salario = str(novo_salario).split("R$")
                    novo_salario = float("".join(novo_salario))

        self._salario = novo_salario

    def trabalhar(self):
        print(f'{self.nomeprofissional} está trabalhando...')


class TI(Profissional): # filha (subclasse) da classe "profissional"
    def programar(self):
        return f'{self.nomeprofissional} está programando...'

class RH(Profissional): # filha (subclasse) da classe "profissional"
    def administrar(self, assunto="pessoal"):
        print(f'{self.nomeprofissional} está gerenciado {assunto}')