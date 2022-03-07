from unittest import TestCase

from q2 import *
    
class TestQuestao2Busca(TestCase):
    """
        Nomeclatura: test_quando_..._deve_retornar_...
            def test_quando_..._deve_retornar_...(self):
        Metodos herdados de TestCase:
        |nome:             | Ação:
        |    setUp         |  Antes   de cada teste
        |    tearDown      |  Depois  de cada teste
        |    setUpClass    |  Antes   de todos os testes
        |    tearDownClass |  Depois  de todos os testes
    """
    
    # def teste_quando_array_crescente_deve_retornar_mediana(self):
        # self.assertEqual(hello_world(), 'hello world')
    # def teste_quando_array_decrescente_deve_retornar_mediana(self):
        # 
    
    def setUp(self):
        print("\nTestando Questao2 Busca")
    
    def Teste(self, lista, deslocamento,saida_esperada):
        print(f"Busca d.        - teste: lista: {lista}, deslocamento: {deslocamento}; saida esperada: {saida_esperada}; ", end="")
        saida = buscar_deslocamentos(lista, deslocamento)
        #saida, pares = buscar_deslocamentos(lista, deslocamento)
        print(f"saida:{saida}")
        #print(f"saida:{saida}, pares: {pares}")
        
        self.assertEqual(saida, saida_esperada)

    def teste_Busca_quando_parametros_sao_do_exemplo1_deve_retornar_3(self):
        n = [1, 5, 3, 4, 2]
        x = 2
        
        saida_esperada = 3

        self.Teste(n,x,saida_esperada)

class TestQuestao2BuscaMelhorada(TestCase):
    """
        Nomeclatura: test_quando_..._deve_retornar_...
            def test_quando_..._deve_retornar_...(self):
        Metodos herdados de TestCase:
        |nome:             | Ação:
        |    setUp         |  Antes   de cada teste
        |    tearDown      |  Depois  de cada teste
        |    setUpClass    |  Antes   de todos os testes
        |    tearDownClass |  Depois  de todos os testes
    """
    
    # def teste_quando_array_crescente_deve_retornar_mediana(self):
        # self.assertEqual(hello_world(), 'hello world')
    # def teste_quando_array_decrescente_deve_retornar_mediana(self):
        # 
    
    def setUp(self):
        print("\nTestando Questao2 Busca Melhorada")
    
    def Teste(self, lista, deslocamento,saida_esperada):
        print(f"Busca d. Melhor - teste: lista: {lista}, deslocamento: {deslocamento}; saida esperada: {saida_esperada}; ", end="")
        saida, pares = buscar_deslocamentos_melhorado(lista, deslocamento)
        print(f"saida:{saida}, pares: {pares}")
        
        self.assertEqual(saida, saida_esperada)

    def teste_Busca_quando_parametros_sao_do_exemplo1_deve_retornar_3(self):
        n = [1, 5, 3, 4, 2]
        x = 2
        
        saida_esperada = 3

        self.Teste(n,x,saida_esperada)
