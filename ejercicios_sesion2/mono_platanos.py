from collections import deque

# Definimos el estado inicial y el final
inicial = ((0, 0), (1, 0), "en el suelo")
final = ((2, 2), (2, 2), "alcanzando plátanos")

# Definimos las posiciones válidas de movimiento
movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # derecha, izquierda, abajo, arriba

def es_estado_valido(pos_mono, pos_banqueta, estado_mono):
    # Aquí no hay restricciones en el estado como en otros problemas
    # pero aseguramos que el mono y la banqueta se mantengan en posiciones válidas
    return 0 <= pos_mono[0] < 3 and 0 <= pos_mono[1] < 3 and \
           0 <= pos_banqueta[0] < 3 and 0 <= pos_banqueta[1] < 3

def mover(pos, movimiento):
    return (pos[0] + movimiento[0], pos[1] + movimiento[1])

def obtener_estados_siguientes(estado):
    pos_mono, pos_banqueta, estado_mono = estado
    siguientes_estados = []
    
    if estado_mono == "en el suelo":
        # Mono se mueve
        for movimiento in movimientos:
            nueva_pos_mono = mover(pos_mono, movimiento)
            if es_estado_valido(nueva_pos_mono, pos_banqueta, estado_mono):
                siguientes_estados.append((nueva_pos_mono, pos_banqueta, "en el suelo"))
        
        # Mono mueve la banqueta
        if pos_mono == pos_banqueta:
            for movimiento in movimientos:
                nueva_pos_banqueta = mover(pos_banqueta, movimiento)
                if es_estado_valido(pos_mono, nueva_pos_banqueta, estado_mono):
                    siguientes_estados.append((pos_mono, nueva_pos_banqueta, "en el suelo"))
        
        # Mono se sube a la banqueta
        if pos_mono == pos_banqueta:
            siguientes_estados.append((pos_mono, pos_banqueta, "sobre la banqueta"))

    elif estado_mono == "sobre la banqueta":
        # Mono intenta alcanzar los plátanos
        if pos_mono == (2, 2):  # Suponemos que los plátanos están en (2, 2)
            siguientes_estados.append((pos_mono, pos_banqueta, "alcanzando plátanos"))

    return siguientes_estados

def resolver_problema():
    # Búsqueda en anchura
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
 