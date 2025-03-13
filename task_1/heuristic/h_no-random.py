# ahora, primero se ordenan de mayor a menor, donde mayor es el que cubre más comunas. Luego se va en orden identificando.
# PROBLEMA: los que tienen igual cantidad de comunas, hace que no se ordene con efectividad
# solución: 1) probar otro orden, sigue siendo mayor a menor pero cambiado los iguales
# solución: 2) buscar otra forma de ordenar y tener una lógica para ir viendo.
# duda: ¿para la pt.2 del backtracking es necesario literalmente crear Arbol?

import random

def select_communes(region):
    # Ordenar las comunas por tamaño de mayor a menor
    sorted_region = sorted(enumerate(region), key=lambda x: len(x[1]), reverse=True)
    selected_indexes = []
    covered = set()
    
    for index, communes in sorted_region:
        if len(covered) >= 15:
            break
        if index not in selected_indexes:
            selected_indexes.append(index)
            covered.update(communes)
    
    return selected_indexes, covered

def find_best_selection(region, costs, iterations=10000):
    best_selection = None
    best_covered = None
    best_cost = float('inf')

    for _ in range(iterations):
        selected_indexes, covered = select_communes(region)
        total_cost = sum(costs[i] for i in selected_indexes)

        if total_cost < best_cost: 
            best_cost = total_cost
            best_selection = selected_indexes
            best_covered = covered
    
    return best_selection, best_covered, best_cost

region = [
    {1,2,3,4,13},
    {1,2,4,12,15},
    {1,3,4,5,6,13}, 
    {1,2,3,4,5,12},
    {4,5,12,7,8,9,6,3},
    {3,6,5,9},
    {7,12,15,14,11,10,8},
    {7,8,10,9,5},
    {8,10,11,5,6,9},
    {7,10,11,8,9}, 
    {9,11,10,7,14},
    {15,12,7,5,4,2},
    {1,3,13},
    {7,11,14}, 
    {2,12,7,14,15}
]

costs = [
    60,  
    30, 
    60,  
    70,
    130,
    60,
    70,
    60,
    80, 
    70, 
    50,
    90,
    30, 
    30,
    100
]

best_selection, best_covered, best_cost = find_best_selection(region, costs, iterations=10000)

print("Mejor selección de comunas:", [i + 1 for i in best_selection])
print("Conjunto cubierto:", sorted(best_covered))
print("Costo total de comunas seleccionadas:", best_cost)
