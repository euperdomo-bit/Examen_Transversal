#importar datos
from datos import productos, stock 

def unidades_categoria(categoria):
    total = 0 
    cate_buscada = categoria.lower()

    for cod, datos in productos.items():
        if datos[1].lower() == cate_buscada:
            total += stock[cod][1]
    
    print(f"El total de las unidades que estan disponible es:{total}")

def busqueda_precio(p_min, p_max):
    encontrados = []

    for cod, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]

        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos [cod][0]
            encontrados.append(f"{nombre}-{cod}")
    if encontrados:
        encontrados.sort()

        print(f"Los productos encontrados son los siguientes: {encontrados}")
    else:
        print("No no encuentran productos de ese precio")

def actualizar_precio(codigo, nuevo_precio):
    cod_upper = codigo.upper()
    if cod_upper in stock:
        stock[cod_upper][0] = nuevo_precio
        return True 
    return False 

def agregar_producto(codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro, precio, unidades):
    cod_upper = codigo.upper()
    if cod_upper in productos:
        return False 
    
    bool_importado = True if es_importado.lower() == 's' else False 
    bool_cachorro = True if es_para_cachorro.lower() == 's' else False 
    
    productos [cod_upper] = [nombre, categoria, marca, float(peso_kg), bool_importado, bool_cachorro]
    stock [cod_upper] = [int(precio), int(unidades)] 
    return True

def eliminar_producto(codigo):
    cod_upper = codigo.upper()
    if cod_upper in productos:
        del productos [cod_upper]
        del stock [cod_upper]
        return True 
    return False 

