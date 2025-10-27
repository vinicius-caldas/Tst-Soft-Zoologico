import sys

# --- FUNÇÕES DO ALGORITMO DO ZOOLÓGICO ---

def calcular_preco_ingresso_unitario(idade):
    """Calcula o preço de um único ingresso com base na idade."""
    if 0 <= idade <= 12:
        return 10.00
    elif 13 <= idade <= 59:
        return 30.00
    elif idade >= 60:
        return 15.00
    else:
        return "Erro: Idade inválida."

def calcular_preco_total(idade, quantidade):
    """Calcula o preço total dos ingressos para a compra."""
    if quantidade < 1:
        return "Erro: Quantidade inferior ao mínimo."
    elif quantidade > 5:
        return "Erro: Quantidade excede o máximo."
    
    preco_unitario = calcular_preco_ingresso_unitario(idade)
    
    if isinstance(preco_unitario, str):
        return preco_unitario
    
    return preco_unitario * quantidade

# --- CASOS DE TESTE (Para serem executados pelo CI) ---

casos_de_teste = [
    {"id": "CT-01", "idade": 0, "quantidade": 1, "esperado": 10.00},
    {"id": "CT-02", "idade": 12, "quantidade": 1, "esperado": 10.00},
    {"id": "CT-03", "idade": 13, "quantidade": 1, "esperado": 30.00},
    {"id": "CT-04", "idade": 59, "quantidade": 1, "esperado": 30.00},
    {"id": "CT-05", "idade": 60, "quantidade": 1, "esperado": 15.00},
    {"id": "CT-06", "idade": 25, "quantidade": 0, "esperado": "Erro: Quantidade inferior ao mínimo."},
    {"id": "CT-07", "idade": 25, "quantidade": 6, "esperado": "Erro: Quantidade excede o máximo."},
    {"id": "CT-08", "idade": -5, "quantidade": 3, "esperado": "Erro: Idade inválida."},
    {"id": "CT-09", "idade": 45, "quantidade": 4, "esperado": 120.00}
]

# --- LÓGICA DE EXECUÇÃO E SAÍDA PARA O GITHUB ACTIONS ---

def execute_tests():
    falhas = 0
    total_testes = len(casos_de_teste)
    
    print("--- INICIANDO TESTES UNITÁRIOS PARA CI ---")
    
    for caso in casos_de_teste:
        resultado_obtido = calcular_preco_total(caso["idade"], caso["quantidade"])
        
        # O teste falha se o resultado obtido for diferente do esperado
        if str(resultado_obtido) != str(caso["esperado"]):
            status = "FALHOU"
            falhas += 1
        else:
            status = "APROVADO"

        print(f"[{caso['id']}] Status: {status} | Entrada: Idade={caso['idade']}, Qtd={caso['quantidade']} | Esperado: {caso['esperado']} | Obtido: {resultado_obtido}")

    print(f"\n--- RESULTADO FINAL: {total_testes} TESTES EXECUTADOS. {falhas} FALHAS. ---")
    
    # O código de saída (Exit Code) determina o sucesso/falha do workflow
    return 1 if falhas > 0 else 0

if __name__ == "__main__":
    # Esta linha faz o script retornar o código de falha se houver testes reprovados
    sys.exit(execute_tests())
