def calcular_preco_ingresso_unitario(idade):
    """
    Calcula o preço de um ingresso com base na idade.
    Crianças (até 12 anos) pagam R$ 10,00.
    Adultos (13 a 59 anos) pagam R$ 30,00.
    Idosos (60 anos ou mais) pagam R$ 15,00.
    """
    if 0 <= idade <= 12:
        return 10.00
    elif 13 <= idade <= 59:
        return 30.00
    elif idade >= 60:
        return 15.00
    else:
        # Erro: Idade inválida (negativa ou não esperada)
        return "Erro: Idade inválida."

def calcular_preco_total(idade, quantidade):
    """
    Calcula o preço total dos ingressos para a compra.
    Verifica se a quantidade está entre 1 e 5 (limite máximo por pessoa).
    """
    if quantidade < 1:
        # Erro 0x1: Quantidade inferior ao mínimo
        return "Erro: Quantidade inferior ao mínimo."
    elif quantidade > 5:
        # Erro 0x2: Quantidade excede o máximo
        return "Erro: Quantidade excede o máximo."
    
    preco_unitario = calcular_preco_ingresso_unitario(idade)
    
    if isinstance(preco_unitario, str):
        # Propaga o erro de idade se a função unitária retornou um erro
        return preco_unitario
    
    return preco_unitario * quantidade

# Função para demonstração (Entrada de dados via terminal)
def main():
    try:
    
        idade = int(input("Digite a idade do visitante: "))
        quantidade = int(input("Digite a quantidade de bilhetes (máximo 5): "))
        
        resultado = calcular_preco_total(idade, quantidade)
        
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"O preço total para a compra é: R$ {resultado:.2f}")

    except ValueError:
        print("Erro: A entrada deve ser um número inteiro.")

if __name__ == "__main__":
   
    main()
