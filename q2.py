# Questão 2: quantidade de elementos com diferença de valor(deslocamento)
# Criado em: 28/02/22
# Atualizado em: 06/03/22

# importa função auxilar que verifica se número é inteiro
from def_aux import is_integer

def buscar_deslocamentos(lista, deslocamento):
    """
        buscar_deslocamentos(lista, deslocamento)
        * lista : um vetor de números inteiros
        * deslocamento : um número inteiro
        
        retorna a quantidade de elementos com diferença de valor(deslocamento) entre si
    """

    #1. Filtro de entrada para evitar erros
    #1.1 verifica lista
    #1.1.1 verifica se lista não é vazia
    if (len(lista)==0):
        assert "Lista não pode ser vazia"
    
    #1.1.2 verifica se todos os elementos de lista são números inteiros
    for elemento in lista:
        if (not is_integer(elemento)):
            assert f"O elemento {elemento} não é um número inteiro"
        
    #1.2 verifica se deslocamento é um número inteiro
    if (int(deslocamento)):
        assert f"O deslocamento precisar ser um número inteiro, recebi: {deslocamento}"

    #2. criar uma variável auxiliar (cont) para contar a quantidade de pares encontrados
    cont = 0
    #3. para cada elemento de lista:
    for elemento1 in lista: 
        #3.1 comparar com todos os outros elementos
        for elemento2 in lista: 
            #3.2 se a diferença entre os elementos for igual a deslocamento, 
            if ( (elemento1-elemento2) == deslocamento ):
                #então soma mais um na variável cont.
                cont += 1
    
    #4. retorna a quantidade de pares encontrados
    return cont

def buscar_deslocamentos_melhorado(lista, deslocamento):
    """
        buscar_deslocamentos(lista, deslocamento)
        * lista : um vetor de números inteiros
        * deslocamento : um número inteiro
        
        retorna:
            * a quantidade de elementos com diferença de valor(deslocamento) entre si
            * lista com os pares com diferença de valor(deslocamento) entre si
    """

    #1. Filtro de entrada para evitar erros
    
    #1.1 verifica lista
    
    #1.1.1 verifica se lista não é vazia
    if (len(lista)==0):
        assert "Lista não pode ser vazia"
 
    #1.1.2 verifica se todos os elementos de lista são números inteiros
    for elemento in lista:
        if (not is_integer(elemento)):
            assert f"O elemento {elemento} não é um número inteiro"

    #1.2 verifica se deslocamento é um número inteiro
    if (int(deslocamento)):
        assert f"O deslocamento precisar ser um número inteiro, recebi: {deslocamento}"

    #2. criar uma variável auxiliar 
    pares = [] # armazena os pares encontrados
    
    #3. para cada elemento de lista:
    for elemento1 in lista: 
        #3.1 comparar com todos os outros elementos
        for elemento2 in lista: 
            #3.2 se a diferença entre os elementos for igual a deslocamento, 
            if ( (elemento1 - elemento2) == deslocamento ):
                #então adiciona os elementos na lista de pares.
                pares.append([elemento1, elemento2])
           
    #4. retorna a quantidade de pares encontrados e os pares
    return len(pares), pares
    
