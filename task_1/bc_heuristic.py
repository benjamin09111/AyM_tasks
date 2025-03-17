"""
Heurística:
Ordenaremos las comunas antes de iniciar el backtracking según su eficiencia de cobertura, definida como:

Eficiencia
=
Cantidad de comunas cubiertas
Costo de la comuna
Eficiencia= 
Costo de la comuna
Cantidad de comunas cubiertas
​
 
Esto significa que exploraremos primero aquellas comunas que cubren más comunas por unidad de costo, lo que aumenta las posibilidades de encontrar una solución óptima más rápido.
"""

def backtracking(region, costs, index, selected, covered, current_cost, best):
    if len(covered) == 15:  # Si se cubren todas las comunas, evaluar solución
        if current_cost < best[0]:  # Mejor solución encontrada
            best[0] = current_cost
            best[1] = selected[:]
        return
    
    if index >= len(region) or current_cost >= best[0]:  # Criterios de poda
        return
    
    # Opción 1: Incluir esta comuna
    new_covered = covered | region[index]  # Unimos las comunas cubiertas
    selected.append(index)
    backtracking(region, costs, index + 1, selected, new_covered, current_cost + costs[index], best)
    selected.pop()  # Deshacer la decisión

    # Opción 2: No incluir esta comuna
    backtracking(region, costs, index + 1, selected, covered, current_cost, best)


def find_best_selection(region, costs):
    # Ordenamos por eficiencia: (cantidad de comunas cubiertas / costo)
    efficiency = [(i, len(region[i]) / costs[i]) for i in range(len(region))]
    efficiency.sort(key=lambda x: x[1], reverse=True)  # Ordenamos de mayor a menor eficiencia
    
    # Reordenamos region y costs según la eficiencia calculada
    sorted_indices = [i for i, _ in efficiency]
    sorted_region = [region[i] for i in sorted_indices]
    sorted_costs = [costs[i] for i in sorted_indices]
    
    best = [float('inf'), []]  # [Mejor costo encontrado, Mejor selección]
    backtracking(sorted_region, sorted_costs, 0, [], set(), 0, best)
    
    # Convertimos los índices ordenados de vuelta a los originales
    best_selection_original = [sorted_indices[i] for i in best[1]]
    return best_selection_original, best[0]


region = [
    {1,2,3,4,13}, {1,2,4,12,15}, {1,3,4,5,6,13}, {1,2,3,4,5,12},
    {4,5,12,7,8,9,6,3}, {3,6,5,9}, {7,12,15,14,11,10,8}, {7,8,10,9,5},
    {8,10,11,5,6,9}, {7,10,11,8,9}, {9,11,10,7,14}, {15,12,7,5,4,2},
    {1,3,13}, {7,11,14}, {2,12,7,14,15}
]

costs = [
    60, 30, 60, 70, 130, 60, 70, 60, 80, 70, 50, 90, 30, 30, 100
]

best_selection, best_cost = find_best_selection(region, costs)
print("Mejor selección de comunas:", [i + 1 for i in best_selection])
print("Costo total mínimo:", best_cost)
