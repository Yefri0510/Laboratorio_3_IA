# Laboratorio_3_IA
* Yefri Stiven Barrero Solano - 23230392
* Jose Alejandro Mesa Chavez - 2291048
* Juan David Becerra Pulio - 2283133

# Maximización de una Función Cuadrática en un Intervalo Cerrado

## Fundamentos Matemáticos

### Función Cuadrática
La función analizada es:
\[ f(x) = x^2 - 3x + 4 \]

Esta es una **parábola convexa** (abre hacia arriba) ya que el coeficiente de \(x^2\) es positivo (\(a = 1 > 0\)).

### Teorema del Valor Extremo
Utilizamos el **Teorema del Valor Extremo** de Weierstrass, que establece que:
> "Toda función continua en un intervalo cerrado y acotado alcanza sus valores máximo y mínimo en dicho intervalo."

Dado que:
- \(f(x)\) es continua (por ser un polinomio)
- Trabajamos en un intervalo cerrado \([x_{\text{min}}, x_{\text{max}}]\)

Podemos garantizar la existencia de valores máximo y mínimo dentro del intervalo.

## Implementación

### Paso 1: Definición de la Función y el Intervalo

```python
def f(x):
    return x**2 - 3*x + 4

# Definir el intervalo cerrado
x_min = 0  # Límite inferior
x_max = 3  # Límite superior
```

### Paso 2: Evaluación en los Extremos del Intervalo

Dado que la función es convexa, el **máximo** en un intervalo cerrado necesariamente ocurrirá en uno de los extremos:

```python
# Evaluar la función en los extremos
f_min = f(x_min)  # f(0) = 4
f_max = f(x_max)  # f(3) = 4
```

### Paso 3: Determinación del Máximo

```python
# Comparar valores en los extremos
if f_min > f_max:
    x_maximo = x_min
    f_maximo = f_min
else:
    x_maximo = x_max
    f_maximo = f_max
```

### Paso 4: Visualización de Resultados

Se genera una gráfica que muestra:
- La función en el intervalo extendido
- Los límites del intervalo (líneas verticales punteadas)
- El punto máximo identificado

## Resultados Obtenidos

Para el intervalo \([0, 3]\):

- **Valor máximo**: \(f(x) = 4\)
- **Posiciones del máximo**: \(x = 0\) y \(x = 3\)
- **Interpretación**: La función alcanza el mismo valor máximo en ambos extremos del intervalo

### Análisis del Comportamiento

La función \(f(x) = x^2 - 3x + 4\) tiene:
- **Vértice**: En \(x = 1.5\) (mínimo de la parábola)
- **Simetría**: La función es simétrica respecto al vértice
- **En el intervalo [0, 3]**: Los extremos están equidistantes del vértice, por lo que alcanzan el mismo valor

## Métodos Alternativos para Funciones No Cuadráticas

Para funciones más complejas (no cuadráticas), se recomienda:

### Método 1: Optimización Numérica con SciPy

```python
from scipy.optimize import minimize

# Minimizar la negación de la función para encontrar el máximo
result = minimize(lambda x: -f(x), x0=0, bounds=[(x_min, x_max)])
x_maximo = result.x[0]
f_maximo = f(x_maximo)
```

### Método 2: Muestreo y Búsqueda Directa

```python
# Evaluar en múltiples puntos del intervalo
x_samples = np.linspace(x_min, x_max, 1000)
y_samples = f(x_samples)
x_maximo = x_samples[np.argmax(y_samples)]
f_maximo = np.max(y_samples)
```
# Algoritmo Genético para el Problema del Viajante (TSP)

## Descripción del Problema

El **Problema del Viajante (TSP - Traveling Salesman Problem)** es un desafío clásico en optimización combinatoria que consiste en encontrar la ruta más corta posible que visite cada ciudad exactamente una vez y regrese al punto de origen. Este problema pertenece a la clase de problemas NP-duros, lo que significa que no existe un algoritmo eficiente para resolverlo en tiempo polinomial cuando el número de ciudades es grande.

## Enfoque con Algoritmo Genético

### Fundamentos de los Algoritmos Genéticos

Los algoritmos genéticos son técnicas de búsqueda heurística inspiradas en los principios de la evolución natural y la genética. Estos algoritmos mantienen una población de soluciones candidatas y aplican operadores de selección, cruce y mutación para evolucionar hacia soluciones mejores a lo largo de generaciones sucesivas.

### Implementación Específica para TSP

#### 1. Representación de la Solución

```python
# Cada ruta se representa como una permutación de índices de ciudades
route = [2, 5, 1, 8, 3, 6, 0, 7, 4, 9]
```

Cada individuo en la población es una permutación única que representa el orden de visita de las ciudades.

#### 2. Función de Evaluación (Fitness)

```python
def total_distance(self, route):
    return sum(self.distance(self.cities[route[i]], 
                            self.cities[route[i+1]]) 
               for i in range(len(route)-1)) + self.distance(self.cities[route[-1]], self.cities[route[0]])
```

La función objetivo calcula la distancia total de la ruta, incluyendo el retorno a la ciudad inicial. El fitness se define como el inverso de esta distancia, por lo que rutas más cortas tienen mayor fitness.

#### 3. Operador de Cruce (Crossover)

Se implementa el **cruce ordenado (Ordered Crossover - OX)**:

```python
def ordered_crossover(self, parent1, parent2):
    # Seleccionar segmento del primer padre
    # Completar con genes del segundo padre manteniendo el orden
```

Este operador preserva el orden relativo de las ciudades, crucial para mantener rutas válidas.

#### 4. Operador de Mutación

```python
def swap_mutation(self, route):
    # Intercambiar dos ciudades aleatorias en la ruta
```

La mutación por intercambio introduce diversidad en la población, explorando nuevas configuraciones.

#### 5. Selección de Padres

```python
def select_parents(self, population, fitnesses):
    # Selección por torneo de tamaño 3
```

La selección por torneo favorece individuos con mejor fitness mientras mantiene cierta diversidad.

## Parámetros del Algoritmo

- **Tamaño de población**: 100 individuos
- **Número de generaciones**: 500 iteraciones
- **Tasa de mutación**: 10% de probabilidad
- **Tamaño del torneo**: 3 individuos

## Proceso Evolutivo

### Inicialización
1. Generar población inicial de rutas aleatorias
2. Calcular fitness de cada individuo

### Bucle Principal (por generaciones)
1. **Evaluación**: Calcular fitness de toda la población
2. **Selección**: Escoger padres para reproducción
3. **Recombinación**: Aplicar cruce ordenado
4. **Mutación**: Aplicar mutación por intercambio
5. **Reemplazo**: Formar nueva generación
6. **Elitismo implícito**: Conservar la mejor solución encontrada

### Criterio de Terminación
- Alcanzar el número máximo de generaciones
- Podría extenderse con criterios de convergencia

## Análisis de Resultados

### Métricas de Evaluación
- **Distancia mínima**: Mejor solución encontrada
- **Convergencia**: Evolución del fitness a través de generaciones
- **Calidad de solución**: Comparación con soluciones conocidas (cuando sea posible)

### Visualización
La función `plot_route` genera una representación gráfica que muestra:
- Ubicación de las ciudades en el plano 2D
- Secuencia de visita según la mejor ruta encontrada
- Distancia total de la ruta óptima

## Características del Algoritmo

### Ventajas
- **No requiere información del gradiente**: Apropiado para problemas discretos
- **Búsqueda paralela**: Explora múltiples regiones del espacio de soluciones
- **Robustez**: Funciona bien en espacios de búsqueda complejos
- **Flexibilidad**: Fácil adaptación a variantes del problema TSP

### Limitaciones
- **Convergencia a óptimos locales**: Puede quedar atrapado en soluciones subóptimas
- **Dependencia de parámetros**: El rendimiento varía con la configuración
- **Sin garantía de optimalidad**: No asegura encontrar la solución global óptima

## Posibles Mejoras

1. **Operadores avanzados**: Implementar otros operadores de cruce (PMX, CX)
2. **Estrategias adaptativas**: Ajustar tasas de mutación y cruce dinámicamente
3. **Híbridación**: Combinar con búsqueda local (2-opt, 3-opt)
4. **Elitismo explícito**: Preservar los mejores individuos entre generaciones
5. **Población estructurada**: Usar modelos de islas o vecindarios

## Aplicaciones Prácticas

El TSP tiene numerosas aplicaciones en el mundo real:
- **Logística y distribución**: Optimización de rutas de reparto
- **Manufactura**: Secuenciación de operaciones en máquinas
- **Circuitos impresos**: Diseño de rutas para perforación de placas
- **Bioinformática**: Análisis de secuencias genéticas

# Optimización de Horarios Escolares con Algoritmo Genético

## Descripción del Problema

La **optimización de horarios escolares** es un problema complejo de scheduling que involucra la asignación de recursos limitados (profesores, aulas, tiempos) a actividades educativas (clases) considerando múltiples restricciones y preferencias. Este problema pertenece a la clase de problemas NP-completos y requiere balancear diversos factores conflictivos.

## Contexto del Sistema Educativo

### Elementos del Sistema
- **Profesores**: 4 profesores especializados
- **Materias**: 4 disciplinas académicas
- **Grupos**: 3 grupos de estudiantes
- **Horarios**: 6 bloques horarios semanales
- **Preferencias**: Restricciones temporales por materia

## Modelamiento Matemático

### Representación de la Solución
Cada horario se representa como una lista de tuplas:
```
(time_slot, group, teacher, subject)
```
Ejemplo: `("Lun-9:00", "Grupo1", "ProfA", "Matemáticas")`

### Función de Evaluación (Fitness)
La función objetivo considera múltiples criterios:

#### Restricciones Fuertes (Penalizaciones Altas)
- **Conflictos de profesores**: Un profesor no puede estar en dos lugares simultáneamente
- **Disponibilidad de profesores**: Respetar horarios disponibles de cada docente

#### Restricciones Suaves (Penalizaciones Moderadas)
- **Preferencias horarias**: Asignar materias en sus horarios preferidos
- **Balance de carga docente**: Distribuir equitativamente las clases entre profesores
- **Distribución de materias**: Garantizar cobertura balanceada por grupo

## Implementación del Algoritmo Genético

### 1. Inicialización de Población
```python
def create_schedule(self):
    # Genera horarios aleatorios respetando la estructura básica
```

### 2. Función de Fitness
```python
def evaluate_schedule(self, schedule):
    # Evalúa múltiples dimensiones de calidad del horario
```

**Componentes de evaluación:**
- **Penalización por superposición**: -100 puntos por cada conflicto
- **Horarios no preferidos**: -10 puntos por asignación inadecuada
- **Disponibilidad incumplida**: -50 puntos por cada violación
- **Desequilibrio docente**: -5 puntos por desviación del promedio
- **Distribución inequitativa de materias**: -3 puntos por desbalance

### 3. Operadores Genéticos

#### Selección por Torneo
```python
def select_parents(self, population, fitnesses):
    # Torneo de tamaño 3 para selección de padres
```

#### Cruce (Crossover)
```python
def crossover(self, parent1, parent2):
    # Cruce en un punto para combinar horarios
```

#### Mutación
```python
def mutate(self, schedule, mutation_rate):
    # Modifica aleatoriamente profesor o materia en asignaciones
```

### 4. Estrategia Evolutiva

- **Población**: 50 individuos
- **Generaciones**: 100 iteraciones
- **Elitismo**: Preserva el mejor individuo
- **Diversificación**: Múltiples tasas de mutación exploradas

## Métricas de Evaluación

### Calidad del Horario
- **Fitness total**: Suma ponderada de todas las restricciones
- **Factibilidad**: Cumplimiento de restricciones fuertes
- **Optimalidad**: Satisfacción de preferencias y balances

### Análisis de Convergencia
- **Evolución del fitness**: Mejora progresiva a través de generaciones
- **Comparativa de parámetros**: Rendimiento con diferentes tasas de mutación

## Análisis de Restricciones

### Restricciones Implementadas

1. **Restricciones de Integridad**
   - Cada grupo tiene exactamente una clase por horario
   - Todas las materias deben ser asignadas

2. **Restricciones de Recursos**
   - No superposición de profesores
   - Disponibilidad de profesores en horarios

3. **Restricciones de Preferencia**
   - Horarios preferidos para materias específicas
   - Balance de carga de trabajo docente

4. **Restricciones de Calidad**
   - Distribución equitativa de materias por grupo
   - Optimización global del horario

## Visualización y Análisis

### Comparativa de Parámetros
El código incluye análisis comparativo de diferentes tasas de mutación:
- **Tasa baja (0.01)**: Explotación intensiva, convergencia rápida
- **Tasa media (0.1)**: Balance entre exploración y explotación
- **Tasa alta (0.3)**: Exploración extensiva, evita óptimos locales

### Representación Gráfica
- **Curvas de convergencia**: Evolución del fitness por generación
- **Comparación visual**: Rendimiento relativo de diferentes configuraciones

## Características del Algoritmo

### Ventajas del Enfoque
- **Manejo de múltiples restricciones**: Evalúa simultáneamente diversos criterios
- **Flexibilidad**: Fácil incorporación de nuevas restricciones
- **Robustez**: Funciona bien en espacios de búsqueda complejos
- **Soluciones factibles**: Genera horarios operativamente válidos

### Limitaciones y Desafíos
- **Calibración de parámetros**: Sensibilidad a tasas de mutación y cruce
- **Tiempo de cómputo**: Requiere múltiples generaciones para converger
- **Óptimos locales**: Puede estancarse en soluciones subóptimas

## Mejoras Potenciales

### Técnicas Avanzadas
1. **Operadores especializados**: Cruce y mutación específicos para scheduling
2. **Búsqueda local**: Aplicar optimizaciones locales post-evolución
3. **Algoritmos híbridos**: Combinar con otras técnicas de optimización
4. **Restricciones dinámicas**: Adaptar pesos según prioridades institucionales

### Extensiones Funcionales
1. **Restricciones de aulas**: Considerar disponibilidad de espacios físicos
2. **Preferencias estudiantiles**: Incorporar necesidades de los estudiantes
3. **Horarios complejos**: Manejar diferentes tipos de clases (teóricas, prácticas)
4. **Múltiples períodos**: Optimizar para semestres completos

## Aplicaciones Prácticas

### Contextos Educativos
- **Escuelas y colegios**: Optimización de horarios académicos
- **Universidades**: Scheduling de cursos y facultades
- **Centros de formación**: Organización de programas educativos

### Beneficios Institucionales
- **Eficiencia operativa**: Mejor utilización de recursos
- **Satisfacción docente**: Respeto a preferencias y disponibilidades
- **Calidad educativa**: Distribución balanceada de materias
- **Reducción de conflictos**: Minimización de solapamientos

## Implementación y Uso

### Configuración Flexible
El sistema permite fácil adaptación a:
- Diferentes números de profesores, materias y grupos
- Variados bloques horarios y preferencias
- Distintas restricciones institucionales

### Escalabilidad
La arquitectura soporta:
- Problemas de mayor dimensión
- Restricciones adicionales
- Criterios de evaluación más complejos

Este sistema demuestra cómo los algoritmos evolutivos pueden resolver problemas complejos de scheduling en entornos educativos, proporcionando horarios optimizados que balancean múltiples objetivos conflictivos mientras garantizan la factibilidad operativa.
