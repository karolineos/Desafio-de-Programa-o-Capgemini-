# Questão 3: criptografia de texto
# Criado em: 28/02/22
# Atualizado em: 06/03/22

# importa sqrt (raiz quadrada) e ceil (arredondar pra cima)
from math import sqrt, ceil
# importa função auxilar que verifica se variavel é texto
from def_aux import is_string

def encriptar(texto):
    """função que recebe um texto e retorna o mesmo criptografado"""

    #1. Filtro de entrada para evitar erros
    #1.1 Verifica se texto é uma string
    #1.1 Se texto é vazio, retorna texto
    
    #2. remove os espaços em branco do texto
    texto = texto.replace(" ","")
    
    #3. sobre a grade
    #3.1 Calcula o tamanho da grade (valor de n)
    n = ceil(sqrt(len(texto)))
    
    #3.2 Cria a grade 
    grade = [["" for _ in range(n)] for __ in range(n)]
    
    #4. insere o texto na grade, no sentido vertical, 
    #   de cima para baixo, da esquerda para a direita.
    for j in range(n): #j = coluna
        for i in range(n): #i = linha
            try: 
                elemento,texto = texto[0],texto[1:]
            except:
                elemento = ""
            finally:
                #linha.append(elemento)
                grade[i][j] = elemento    
    #5. transforma a grade em um texto
    texto_criptografado = " ".join(["".join(x) for x in grade])
    
    #6. retorna o resultado da transformação
    return texto_criptografado
