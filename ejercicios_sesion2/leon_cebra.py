from collections import deque

# Definimos el estado inicial y el final
inicial = ('izq', 'izq', 'izq')
final = ('der', 'der', 'der')

# Posibles movimientos
movimientos = ['leon', 'cebra']

def es_estado_valido(leon, cebra, barca):
    # El estado es válido si la cebra no está sola con el león sin la barca
    if leon == cebra and barca != cebra:
        return False  # La cebra y el león están solos sin la barca: peligro
    return True

def obtener_estados_siguientes(estado):
    leon, cebra, barca = estado
    siguientes_estados = []
    
    # Movimiento si el león cruza solo
    if barca == 'izq' and leon == 'izq':
        nuevo_estado = ('der', cebra, 'der')
        if es_estado_valido(*nuevo_estado):
            siguientes_estados.append(nuevo_estado)
    elif barca == 'der' and leon == 'der':
        nuevo_estado = ('izq', cebra, 'izq')
        if es_estado_valido(*nuevo_estado):
            siguientes_estados.append(nuevo_estado)
    
    # Movimiento si la cebra cruza sola
    if barca == 'izq' and cebra == 'izq':
        nuevo_estado = (leon, 'der', 'der')
        if es_estado_valido(*nuevo_estado):
            siguientes_estados.append(nuevo_estado)
    elif barca == 'der' and cebra == 'der':
        nuevo_estado = (leon, 'izq', 'izq')
        if es_estado_valido(*nuevo_estado):
            siguientes_estados.append(nuevo_estado)
    
    return siguientes_estados

def resolver_problema():
    # Búsqueda en anchura, BFS
    cola = deque([(inicial, [inicial])])
    visitados = set([inicial])

    while cola:
        estado_actual, camino = cola.popleft()

        if estado_actual == final:
            return camino  # Se encontró una solución
        
        for siguiente_estado in obtener_estados_siguientes(estado_actual):
            if siguiente_estado not in visitados:
                visitados.add(siguiente_estado)
                cola.append((siguiente_estado, camino + [siguiente_estado]))
    
    return None  # No se encontró solución

# Ejecutamos la resolución del problema
solucion = resolver_problema()

if solucion:
    print("Solución encontrada:")
    for paso in solucion:
        print(paso)
else:
    print("No se encontró solución.")
