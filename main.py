import validaciones 
import funciones 

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Ingrese opción: ").strip()
        
        if opcion == "1":
            cate = input("Ingrese la categoria a consultar: ")
            funciones.unidades_categoria(cate)
            
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese un precio minimo: "))
                    p_max = int(input("Ingrese un precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar valores validos")
                except ValueError:
                    print("Debe ingresar valores enteros")
            funciones.busqueda_precio(p_min, p_max)
            
        elif opcion == "3":
            while True:
                cod = input("Ingrese codigo del producto: ")
                while True:
                    try:
                        n_precio = int(input("Ingrese nuevo precio: "))
                        if n_precio > 0:
                            break
                        print("El precio debe ser un numero entero mayor que cero")
                    except ValueError:
                        print("Debe ingresar un valor que sea entero")
                
                if funciones.actualizar_precio(cod, n_precio):
                    print("Precio actualizado con exito")
                else:
                    print("El codigo no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    break
                    
        elif opcion == "4":
            cod = input("Ingrese el codigo del producto: ")
            if not validaciones.validar_codigo(cod):
                print("El codigo no es valido")
                continue
                
            nom = input("Ingrese nombre: ")
            if not validaciones.validar_texto(nom):
                print("Nombre no válido.")
                continue
                
            cate = input("Ingrese categoria: ")
            if not validaciones.validar_texto(cate):
                print("Categoría no válida.")
                continue
                
            mar = input("Ingrese marca: ")
            if not validaciones.validar_texto(mar):
                print("Marca no válida.")
                continue
                
            peso = input("Ingrese peso (kg): ")
            if not validaciones.validar_peso(peso):
                print("Peso no válido.")
                continue
                
            imp = input("¿Es importado? (s/n): ")
            if not validaciones.validar_sn(imp):
                print("Respuesta no valida (debe ser s/n)")
                continue
                
            cach = input("¿Es para cachorro? (s/n): ")
            if not validaciones.validar_sn(cach):
                print("Respuesta no es valida (debe ser s/n)")
                continue
                
            pre = input("Ingrese precio: ")
            if not validaciones.validar_precio_val(pre):
                print("Precio no es valido")
                continue
                
            uni = input("Ingrese las unidades: ")
            if not validaciones.validar_unidades(uni):
                print("Unidades no validas")
                continue
            
            if funciones.agregar_producto(cod, nom, cate, mar, peso, imp, cach, pre, uni):
                print("Producto agregado exitosamente")
            else:
                print("El codigo ya existe")
                
        elif opcion == "5":
            cod = input("Ingrese codigo del producto que desea eliminar: ")
            if funciones.eliminar_producto(cod):
                print("Producto eliminado exitosamente")
            else:
                print("El codigo no existe")
                
        elif opcion == "6":
            print("Programa ha finalizado")
            break
            
        else:
            print("seleccione una opcion valida")

if __name__ == "__main__":
    main()