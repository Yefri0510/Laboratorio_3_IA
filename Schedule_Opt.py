import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class ScheduleOptimizer:
    
    def __init__(self):
        self.teachers = ["ProfA", "ProfB", "ProfC", "ProfD"]
        self.subjects = ["Matemáticas", "Ciencias", "Historia", "Arte"]
        self.groups = ["Grupo1", "Grupo2", "Grupo3"]
        self.times_slots = ["Lun-9:00", "Lun-11:00", "Mar-9:00", "Mar-11:00",
                            "Mié-9:00", "Mié-11:00"]
        self.preferences = {
            "Matemáticas": ["9:00"],
            "Arte": ["11:00"]
        }
        self.teacher_availability = {t: self.times_slots for t in self.teachers}
        
    def create_schedule(self):
        schedule = []
        for time in self.times_slots:
            for group in self.groups:
                teacher = np.random.choice(self.teachers)
                subject = np.random.choice(self.subjects)
                schedule.append((time, group, teacher, subject))
        return schedule
    
    def evaluate_schedule(self, schedule):
        score = 0
        # Penalizar superposiciones de profesores
        time_teacher = defaultdict(list)
        for entry in schedule:
            time, group, teacher, subject = entry
            time_teacher[time].append(teacher)
        for time, teachers in time_teacher.items():
            if len(teachers) != len(set(teachers)):
                score -= 100 * (len(teachers) - len(set(teachers)))
        # Penalizar horarios no preferidos
        for entry in schedule:
            time, group, teacher, subject = entry
            if subject in self.preferences:
                pref = self.preferences[subject]
                if all(p not in time for p in pref):
                    score -= 10
        # Penalizar no disponibilidad (aunque por default todos disponibles)
        for entry in schedule:
            time, group, teacher, subject = entry
            if time not in self.teacher_availability[teacher]:
                score -= 50
        # Balance de profesores
        teacher_count = defaultdict(int)
        for entry in schedule:
            teacher_count[entry[2]] += 1
        avg_teacher = len(schedule) / len(self.teachers)
        for count in teacher_count.values():
            score -= 5 * abs(count - avg_teacher)
        # Balance de materias por grupo
        group_subject = defaultdict(lambda: defaultdict(int))
        for entry in schedule:
            group_subject[entry[1]][entry[3]] += 1
        avg_subject = len(self.times_slots) / len(self.subjects)
        for g in self.groups:
            for s in self.subjects:
                score -= 3 * abs(group_subject[g][s] - avg_subject)
        return score
    
    def select_parents(self, population, fitnesses):
        tournament_size = 3
        idx = np.random.choice(len(population), tournament_size, replace=False)
        best_idx = idx[np.argmax([fitnesses[i] for i in idx])]
        return population[best_idx]
    
    def crossover(self, parent1, parent2):
        size = len(parent1)
        point = np.random.randint(1, size)
        child = parent1[:point] + parent2[point:]
        return child
    
    def mutate(self, schedule, mutation_rate):
        for i in range(len(schedule)):
            if np.random.random() < mutation_rate:
                time, group, teacher, subject = schedule[i]
                if np.random.random() < 0.5:
                    teacher = np.random.choice(self.teachers)
                else:
                    subject = np.random.choice(self.subjects)
                schedule[i] = (time, group, teacher, subject)
        return schedule
    
    def genetic_algorithm(self, pop_size=50, generations=100, mutation_rate=0.1):
        population = [self.create_schedule() for _ in range(pop_size)]
        best_fitnesses = []
        best_schedule = None
        best_fitness = float('-inf')
        for gen in range(generations):
            fitnesses = [self.evaluate_schedule(s) for s in population]
            current_best_idx = np.argmax(fitnesses)
            current_best_fitness = fitnesses[current_best_idx]
            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                best_schedule = population[current_best_idx]
            best_fitnesses.append(best_fitness)
            elite = population[current_best_idx]
            new_population = [elite]
            while len(new_population) < pop_size:
                p1 = self.select_parents(population, fitnesses)
                p2 = self.select_parents(population, fitnesses)
                child = self.crossover(p1, p2)
                child = self.mutate(child, mutation_rate)
                new_population.append(child)
            population = new_population
        return best_schedule, best_fitnesses

def print_schedule(schedule, times_slots, groups):
    print("Tiempo\t\tGrupo1\t\t\tGrupo2\t\t\tGrupo3")
    for time in times_slots:
        row = [time]
        for group in groups:
            for entry in schedule:
                if entry[0] == time and entry[1] == group:
                    row.append(f"{entry[2]} - {entry[3]}")
                    break
        print("\t\t".join(row))

def run_and_visualize(mutation_rates=[0.01, 0.1, 0.3]):
    optimizer = ScheduleOptimizer()
    convergences = {}
    for rate in mutation_rates:
        print(f"\nEjecutando con tasa de mutación {rate}")
        best_schedule, fitnesses = optimizer.genetic_algorithm(pop_size=50, generations=100, mutation_rate=rate)
        convergences[rate] = fitnesses
        print(f"Mejor fitness: {fitnesses[-1]}")
        print("Mejor horario:")
        print_schedule(best_schedule, optimizer.times_slots, optimizer.groups)
    plt.figure(figsize=(10, 6))
    for rate, fits in convergences.items():
        plt.plot(fits, label=f"Tasa de mutación {rate}")
    plt.xlabel("Generaciones")
    plt.ylabel("Fitness")
    plt.title("Convergencia del Fitness por Tasa de Mutación")
    plt.legend()
    plt.grid(True)
    plt.show()

run_and_visualize()