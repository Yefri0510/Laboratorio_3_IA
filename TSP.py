import numpy as np
import matplotlib.pyplot as plt

class TSPGeneticAlgorithm:
    
    def __init__(self, num_cities):
        self.cities = self.generate_cities(num_cities)
    
    def generate_cities(self, n):
        return [(np.random.random(), np.random.random()) for _ in range(n)]
    
    def distance(self, city1, city2):
        return np.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)
    
    def total_distance(self, route):
        return sum(self.distance(self.cities[route[i]], 
                                self.cities[route[i+1]]) 
                   for i in range(len(route)-1)) + self.distance(self.cities[route[-1]], self.cities[route[0]])
    
    def fitness(self, route):
        return 1 / self.total_distance(route)
    
    def ordered_crossover(self, parent1, parent2):
        size = len(parent1)
        # Elegir dos puntos de corte aleatorios
        start, end = sorted(np.random.choice(range(size), 2, replace=False))
        # Obtener el segmento del primer padre
        child = [None] * size
        child[start:end] = parent1[start:end]
        # Llenar el resto con genes del segundo padre, manteniendo el orden
        remaining = [x for x in parent2 if x not in child[start:end]]
        j = 0
        for i in range(size):
            if child[i] is None:
                child[i] = remaining[j]
                j += 1
        return child
    
    def swap_mutation(self, route):
        # Seleccionar dos índices aleatorios
        idx1, idx2 = np.random.choice(len(route), 2, replace=False)
        # Intercambiar las ciudades en esos índices
        route[idx1], route[idx2] = route[idx2], route[idx1]
        return route
    
    def generate_population(self, pop_size):
        # Generar una población de rutas aleatorias
        return [np.random.permutation(len(self.cities)).tolist() for _ in range(pop_size)]
    
    def select_parents(self, population, fitnesses):
        # Selección por torneo
        tournament_size = 3
        idx = np.random.choice(len(population), tournament_size, replace=False)
        best_idx = idx[np.argmax([fitnesses[i] for i in idx])]
        return population[best_idx]
    
    def genetic_algorithm(self, pop_size=100, generations=500, mutation_rate=0.1):
        # Inicializar población
        population = self.generate_population(pop_size)
        best_route = None
        best_distance = float('inf')
        
        for generation in range(generations):
            # Calcular aptitudes
            fitnesses = [self.fitness(route) for route in population]
            
            # Encontrar la mejor ruta de la generación actual
            current_best_idx = np.argmax(fitnesses)
            current_best_distance = 1 / fitnesses[current_best_idx]
            if current_best_distance < best_distance:
                best_distance = current_best_distance
                best_route = population[current_best_idx].copy()
            
            # Crear nueva población
            new_population = []
            for _ in range(pop_size):
                # Seleccionar padres
                parent1 = self.select_parents(population, fitnesses)
                parent2 = self.select_parents(population, fitnesses)
                # Aplicar cruce
                child = self.ordered_crossover(parent1, parent2)
                # Aplicar mutación con cierta probabilidad
                if np.random.random() < mutation_rate:
                    child = self.swap_mutation(child)
                new_population.append(child)
            
            population = new_population
            
            # Imprimir progreso cada 100 generaciones
            if generation % 100 == 0:
                print(f"Generación {generation}: Mejor distancia = {best_distance:.4f}")
        
        return best_route, best_distance

def plot_route(cities, route):
    plt.figure(figsize=(10,6))
    x = [cities[i][0] for i in route] + [cities[route[0]][0]]  # Corregir bucle al inicio
    y = [cities[i][1] for i in route] + [cities[route[0]][1]]  # Corregir bucle al inicio
    plt.plot(x, y, 'o--')
    plt.title(f'Ruta óptima - Distancia total: {TSP.total_distance(route):.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

np.random.seed(42)  # Para reproducibilidad
TSP = TSPGeneticAlgorithm(num_cities=10)
best_route, best_distance = TSP.genetic_algorithm(pop_size=100, generations=500, mutation_rate=0.1)
print(f"Mejor ruta encontrada: {best_route}")
print(f"Distancia total: {best_distance:.4f}")
plot_route(TSP.cities, best_route)
