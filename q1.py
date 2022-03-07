# Questão 1. Encontrar a mediana de uma lista
# Criado em: 28/02/22
# Atualizado em: 06/03/22

# para mais informações acesse o readme.md ou q1.md

def mediana(lista):
    """ 
        Encontra a mediana de uma lista de números, com quantidade de elementos ímpar
        
        mediana(lista)
            Com lista sendo um vetor unitário de N posições,
            e N sendo um número ímpar
            
        exemplo:
            mediana([28,10,98]) #28
    """
    # 1. Filtrando entrada
    n = len(lista)
    
    # 1.1 se n for igual a 0, dispara erro
    if (n == 0): 
       assert "Lista vazia, lista precisa ter ao menos um elemento"
    
    # 1.1 verifica se a lista possui número ímpar de elementos
    if (n%2 == 0): 
       assert "Lista precisa ter número ímpar de elementos"

    # 2. ordenar a lista (independente se for crescente ou decrescente)
    lista.sort() # ordena de forma crescente
    
    # 3. retorna o elemento que está no centro da lista
    centro = n//2
    return lista[centro]
    

def mediana_melhorada(lista):
    """ 
        Encontra a mediana de uma lista de números
        
        mediana(lista)
            Com lista sendo um vetor unitário de N posições,
            e N sendo um número ímpar
        
        exemplo:
            mediana([28,10,21,98]) #24.5
    """
    
    # 1. Filtrando entrada
    n = len(lista)
    
    # 1.1 se n for igual a 0, dispara erro
    if (n == 0): 
       assert "Lista vazia, lista precisa ter ao menos um elemento"
    
    # 2. ordenar a lista (independente se for crescente ou decrescente)
    lista.sort() # ordena de forma crescente
    
    # 3. retorna a mediana
   
    #3.1 se n for par, retorna a média dos dois números centrais da lista
    centro = n//2
    if (n%2 == 0):
        return (lista[centro - 1] + lista[centro + 1])/2
    
    # 3.2 se n for ímpar, retorna o elemento que está no centro da lista
    return lista[centro]
    

if (__name__ == "__main__"):
    # exibindo dicas para o uso, caso script executado diretamente (sem importar)
    print("Para calcular a mediana de uma lista use:")
    print("\n\t mediana(lista) (para lista de tamanho ímpar, conforme o desafio)")
    print("\n\t mediana_melhorada(lista) (para mediana de lista com tamanho par ou impar)")
    
