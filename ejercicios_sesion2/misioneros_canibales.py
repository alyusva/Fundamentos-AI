from collections import deque

# Definimos el estado inicial y el final
inicial = (3, 3, 0, 0, 'izq')
final = (0, 0, 3, 3, 'der')

# Posibles movimientos de la barca
movimientos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def es_estado_valido(m_izq, c_izq, m_der, c_der):
    # Verifica si el estado es válido, es decir, que los caníbales no superen a los misioneros
    return (m_izq == 0 or m_izq >= c_izq) and (m_der == 0 or m_der >= c_der) and \
           0 <= m_izq <= 3 and 0 <= c_izq <= 3 and \
           0 <= m_der <= 3 and 0 <= c_der <= 3 #no haya mas M que C en derecha y en izquierda
                                                # no hay mas 3 M o C en ningun lado, ni menos de 0

def obtener_estados_siguientes(estado):
    m_izq, c_izq, m_der, c_der, barca = estado
    siguientes_estados = []
    
    # Verifica hacia dónde se mueve la barca
    if barca == 'izq':  # La barca está en la izquierda
        for m, c in movimientos:
            nuevo_estado = (m_izq - m, c_izq - c, m_der + m, c_der + c, 'der')
            if es_estado_valido(nuevo_estado[0], nuevo_estado[1], nuevo_estado[2], nuevo_estado[3]):
                siguientes_estados.append(nuevo_estado)
    else:  # La barca está en la derecha
        for m, c in movimientos:
            nuevo_estado = (m_izq + m, c_izq + c, m_der - m, c_der - c, 'izq')
            if es_estado_valido(nuevo_estado[0], nuevo_estado[1], nuevo_estado[2], nuevo_estado[3]):
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
