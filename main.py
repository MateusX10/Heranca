from classes import Profissional, TI, RH

pro1 = Profissional("Pedro lagarta augusto dos santos", "adasds",42, "R$1500")
print(pro1.nome)
print(pro1.idade)
print(pro1.area)
print(pro1.salario)
pro1.trabalhar()

ti1 = TI("Pedro", 30, "TI", "R$6500")
print(ti1.nome, ti1.idade, ti1.area, ti1.salario)
ti1.trabalhar()
print(ti1.programar())

rh1 = RH("Laura martins", 45, "RH", "R$9000")
print(rh1.nome, rh1.idade, rh1.area, rh1.salario)
rh1.trabalhar()
rh1.administrar()