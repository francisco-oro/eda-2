def mostrarArreglo(tamaño):
    return [None] * tamaño

def obtenerLlaveNumerica(llave):
    hash = 0
    for char in str(llave):
        hash += ord(char)
    return hash

def H(llaveN):
    return llaveN % 5

def agregar(llave, valor, map, tamaño):
    llave_hash = H(obtenerLlaveNumerica(llave))
    parLlaveValor = [llave, valor]

    if map[llave_hash] is None:
        map[llave_hash] = [parLlaveValor]
        return True
        
    for j, par in enumerate(map[llave_hash]):
        if par[0] == llave:
            par[1] = valor
            return True
            
#Colisiones con direccionamiento abierto
    for j in range(tamaño):
        llaveh = (llave_hash + j) % tamaño
        if map[llaveh] is None:
            map[llaveh] = [parLlaveValor]
            return True

    print("Tabla llena", llave_hash)
    return False

def buscar(llave, map, tamaño):
    llave_hash = H(obtenerLlaveNumerica(llave))
    
    if map[llave_hash] is not None:
        for par in map[llave_hash]:
            if par[0] == llave:
                return par[1]
                
            else:
                for j in range(tamaño):
                    llaveh = (llave_hash + j) % tamaño
                    
                    if map[llaveh] is not None:
                        for par1 in map[llaveh]:
                            if par1[0] == llave:
                                return par1[1]
    
    return None

def showAllElements(map, tamaño): # Función que itera sobre la lista map
    for i in range(tamaño): # Recuperar el índice asociado a cada par valor-clave
        if map[i] is not None:
            for par in map[i]: 
                print(f'Llave: {par[0]}, Valor: {par[1]}, Llave hash: {i}') # Imprimir datos


map = mostrarArreglo(10)

agregar("Hola9", "12213299", map, 10)
agregar("Hola4", 12213214, map, 10)
agregar("Hola1", 1221321, map, 10)
agregar("Hola2", 1221322, map, 10)
agregar("Hola3", 1221323, map, 10)
agregar("Hola5", 1221325, map, 10)
agregar("Hola6", 1221326, map, 10)
agregar("Hola7", 1221327, map, 10)
agregar("Hola8", 1221328, map, 10)
agregar("Hola10", 1221310, map, 10)

showAllElements(map, 10)