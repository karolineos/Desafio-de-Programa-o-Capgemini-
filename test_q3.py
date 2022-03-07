from unittest import TestCase

from q3 import encriptar
    
class TestQuestao3Encriptar(TestCase):
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
        print("\nTestando Questao3 Encriptar")
    
    def Teste(self, s, saida_esperada):
        print(
            f"Encriptar -",
            f"entrada: s: {s};"
            f"saida esperada: {saida_esperada}; ",
            end=""
        )
        saida = encriptar(s)
        print(f"saida:{saida}")
        
        self.assertEqual(saida, saida_esperada)

    def teste_Busca_quando_parametros_sao_do_exemplo1_deve_retornar_omd_luo_an(self):
        s = "ola mundo"
        
        saida_esperada = "omd luo an"

        self.Teste(s,saida_esperada)