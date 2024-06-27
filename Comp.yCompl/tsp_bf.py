import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    number_of_points = len(permutation)

    for i in range(number_of_points):
        total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % number_of_points]]
    
    return total_distance

def find_shortest_route(distance_matrix):
    number_of_points = len(distance_matrix)
    all_permutations = permutations(range(number_of_points))
    min_distance = float('inf')
    best_route = None

    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    return best_route, min_distance

def generate_coordinates(num_points, radius=1):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    coordinates = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]
    return coordinates

def plot_route(route, distance_matrix, coordinates):
    plt.figure(figsize=(10, 8))
    
    x = [coordinates[i][0] for i in route] + [coordinates[route[0]][0]]
    y = [coordinates[i][1] for i in route] + [coordinates[route[0]][1]]
    
    plt.plot(x, y, marker='o')
    
    for i, point in enumerate(route):
        plt.text(x[i], y[i], f'P{point}', fontsize=12, ha='right')
        next_point = (i + 1) % len(route)
        distance = distance_matrix[route[i]][route[next_point]]
        mid_x = (x[i] + x[next_point]) / 2
        mid_y = (y[i] + y[next_point]) / 2
        plt.text(mid_x, mid_y, str(distance), fontsize=10, ha='center', color='blue')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Shortest Route')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Definición de la matriz de distancias
    distance_matrix = [
       [ 19,  35,  19,  95,  89,  13,  96,  10,  38,  44],
       [  5,  91,  95,  12,  93,  43,  81,  62,  15,  50],
       [ 19,  25,  63,  98,  20,  82,  97,  43,  22,  19],
       [ 25,  81,  91,  37,  54,  38,  47,  21,  56,  43],
       [ 62,  89,  32,  13,  32,  14,  25,  45,  54,  73],
       [ 48,  99,  49,  63,  95,  68,  45,  20,  95,   7],
       [100,  44,  30,  79,  22,  22,  81,  82,  30,   8],
       [ 45,  26,  56,  94,  25,  47,   2,   5,  92,  48],
       [ 95,  66,  77,  91,  85,  28,  39,  97,  76,  40],
       [ 57,  57,  54,  91,  17,  51,  56,  77,  21,  20]
    ]

    # Generar coordenadas automáticamente
    num_points = len(distance_matrix)
    coordinates = generate_coordinates(num_points)

    # Encontrar y mostrar la ruta más corta
    best_route, min_distance = find_shortest_route(distance_matrix)
    if best_route:
        print(f"Shortest route: {best_route} with distance {min_distance}")
        
        # Graficar la ruta más corta
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No viable route found!")
