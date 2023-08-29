# Calculadora em Python

continuar = "S"
while continuar == "S":
    
   numero_1 = int(input("\nDigite um número:"))
   numero_2 = int(input("Digite outro número:")) 
   print('''\n O que voce deseja fazer:
	[1] Somar
	[2] Subtrair
	[3] Multiplicar
	[4] Dividir
	
''')

   opção_escolhida = int(input("Digite sua escolha:"))
 
   if opção_escolhida == 1:
       adicao = numero_1 + numero_2   
       print(f"{numero_1} + {numero_2} = {adicao}")    
   elif opção_escolhida == 2:
       subtracao = numero_1 - numero_2
       print(f"{numero_1} - {numero_2} = {subtracao}")
   elif opção_escolhida == 3:
       multiplicacao = numero_1 * numero_2
       print(f"{numero_1} × {numero_2} = {multiplicacao}")
   elif opção_escolhida == 4:
       divisao = numero_1 / numero_2
       print(f"{numero_1} ÷ {numero_2} = {divisao}")
   else:
       print("Digite uma opção valida")

   continuar = str(input('\nDigite a letra [s] para continuar: ')).upper()
