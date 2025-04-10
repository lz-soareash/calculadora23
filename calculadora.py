import math

def bhaskara():
    print("\n formula de Bhaskara ")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    if a == 0:
        print("O valor de a não pode ser zero em uma equação do segundo grau.")
        return
    
    delta = b**2 - 4 * a * c
    print("Delta =", delta)
    
    if delta < 0:
        print("Não existem raízes reais (delta negativo).")
    elif delta == 0:
        x = -b / (2 * a)
        print("Existe uma raiz real:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("As raízes são:")
        print("x1 =", x1)
        print("x2 =", x2)

def pitagoras():
    print("\n Pitágoras (Cálculo da Hipotenusa)")
    cateto1 = float(input("Digite o valor do primeiro cateto: "))
    cateto2 = float(input("Digite o valor do segundo cateto: "))
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("A hipotenusa é:", hipotenusa)

def seno():
    print("\n Cálculo do Seno ")
    angulo = float(input("Digite o ângulo em graus: "))
    rad = math.radians(angulo)
    print("Seno(%.2f°) = %.4f" % (angulo, math.sin(rad)))

def cosseno():
    print("\nCálculo do Cosseno ")
    angulo = float(input("Digite o ângulo em graus: "))
    rad = math.radians(angulo)
    print("Cosseno(%.2f°) = %.4f" % (angulo, math.cos(rad)))

def tangente():
    print("\n=== Cálculo da Tangente ===")
    angulo = float(input("Digite o ângulo em graus: "))
    rad = math.radians(angulo)
    # Verifica se a tangente está definida (evitar ângulos onde o cosseno é zero)
    if math.isclose(math.cos(rad), 0.0, abs_tol=1e-9):
        print("A tangente não está definida para este ângulo.")
    else:
        print("Tangente(%.2f°) = %.4f" % (angulo, math.tan(rad)))

def menu():
    print("Calculadora Multifunções:")
    print("1 - Bhaskara")
    print("2 - Pitágoras")
    print("3 - Seno")
    print("4 - Cosseno")
    print("5 - Tangente")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Digite o número da operação desejada: ").strip()
        
        if opcao == '1':
            bhaskara()
        elif opcao == '2':
            pitagoras()
        elif opcao == '3':
            seno()
        elif opcao == '4':
            cosseno()
        elif opcao == '5':
            tangente()
        elif opcao == '0':
            print("Encerrando a calculadora. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
