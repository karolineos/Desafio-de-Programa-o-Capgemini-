

def is_integer(n):
    """Testa se uma variável é um número inteiro"""
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def is_string(text):
    """Testa se uma variável é do tipo texto"""
    return isinstance(text, str)