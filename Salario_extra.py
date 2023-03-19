salario_inteiro = float(input("Digite o seu salario inteiro: "))
salario_base = float(input("Digite o salário base por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))
taxa_horas_extras = float(input("Digite a taxa de pagamento das horas extras: "))

salario_total = salario_base * horas_trabalhadas
salario_horas_extras = salario_base * taxa_horas_extras * horas_extras
salario_total = salario_horas_extras + salario_inteiro

print("O salário total é:", salario_total)
