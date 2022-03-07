from unittest import TestCase

from q1 import *
    
class TestQuestao1Mediana(TestCase):
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
        print("\nTestando Questao1 Mediana")
    
    def Teste(self, arr, saida_esperada):
        print(f"Mediana     - teste: arr:{arr}; saida esperada: {saida_esperada}; ", end="")
        saida = mediana(arr)
        print(f"saida:{saida}")
        
        self.assertEqual(saida, saida_esperada)

    def teste_Med_quando_parametros_sao_do_exemplo1_deve_retornar_mediana(self):
        arr = [9, 2, 1, 4, 6]
        saida_esperada = 4

        self.Teste(arr,saida_esperada)
   
class TestQuestao1MedianaMelhorada(TestCase):
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
        print("\nTestando Questao1 Mediana Melhorada")
    
    def Teste(self, arr, saida_esperada):
        print(f"Med. Melhor - teste: arr:{arr}; saida esperada: {saida_esperada}; ", end="")
        saida = mediana_melhorada(arr)
        print(f"saida:{saida}")
        
        self.assertEqual(saida, saida_esperada)

    def teste_quando_parametros_sao_do_exemplo1_deve_retornar_mediana(self):
        arr = [9, 2, 1, 4, 6]
        saida_esperada = 4

        self.Teste(arr,saida_esperada)