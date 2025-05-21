
import time

# Déclaration de la variable globale
global_counter = 0

def increment_global(n):
    global_counter = 0
    for _ in range(n):
        global_counter += 1 
    return global_counter

# Declaration de la variable locale

def increment_local(n):
    local_counter = 0  # Variable locale
    for _ in range(n):
        local_counter += 1
    return local_counter


# Fonction pour mesurer le temps d'exécution
def measure_time(fct,n):
    start_time = time.time()
    func= globals()[fct]
    func(n)
    end_time = time.time()
    return end_time - start_time

# Comparaison des performances
increments = [10, 1000, 1000000 ]
for inc in increments:
    elapsed_time = measure_time('increment_global',inc)
    print(f" Non_Compliant : {inc}, elapsed time : {elapsed_time:.6f} secondes")
    elapsed_time = measure_time('increment_local',inc)
    print(f"Compliant : {inc}, elapsed time: {elapsed_time:.6f} secondes")


   
