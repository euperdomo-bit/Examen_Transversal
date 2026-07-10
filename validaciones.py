from datos import productos 

def validar_texto(texto):
    return texto.strip() !=""

def validar_codigo(codigo):
    if not validar_texto(codigo):
        return False
    return codigo.upper() not in productos

def validar_peso(peso_str):
    try:
         val = float(peso_str)
         return val > 0 
    except ValueError:
        return False 
    
def validar_sn(opcion):
    return opcion.lower() in ['s', 'n']

def validar_precio_val(precio_str):
    try:
        val = int(precio_str)
        return val > 0 
    except ValueError:
        return False 
    
def validar_unidades(unidades_str):
    try:
        val = int(unidades_str)
        return val >= 0 
    except ValueError:
        return False
