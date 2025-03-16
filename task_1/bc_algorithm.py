def backtracking(region, costs, index, selected, covered, current_cost, best):
    # si se cubren todas las comunas, se evalúa la solucion
    if len(covered) == 15:
        if current_cost < best[0]:  # Mejor solución encontrada
            best[0] = current_cost
            best[1] = selected[:]
        return
    
    # si se exploran todas las comunas, se termina el algoritmo
    if index >= len(region):
        return

    # si el costo actual ya supera el mejor encontrado, se detiene el algoritmo
    if current_cost >= best[0]:
        return
    
    # Opción 1: Incluir esta comuna
    new_covered = covered | region[index]  # Unimos las comunas cubiertas
    selected.append(index)
    backtracking(region, costs, index + 1, selected, new_covered, current_cost + costs[index], best)
    selected.pop()  # Deshacemos la decisión

    # Opción 2: No incluir esta comuna
    backtracking(region, costs, index + 1, selected, covered, current_cost, best)


def find_best_selection(region, costs):
    best = [float('inf'), []]  # [Mejor costo encontrado, Mejor selección]
    backtracking(region, costs, 0, [], set(), 0, best)
    return best[1], best[0]


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

best_selection, best_cost = find_best_selection(region, costs)

print("Mejor selección de comunas:", [i + 1 for i in best_selection])
print("Costo total mínimo:", best_cost)
