"""

Vas a crear un programa llamado mi_gestor_gastos.py que ayude a una persona a entender sus gastos semanales.
El programa trabajará con datos ficticios y deberá permitir:
Guardar varios gastos en una lista.
Calcular el total de los gastos.
Calcular el gasto medio.
Mostrar qué gastos superan los 20 €.
Mostrar un mensaje indicando si el gasto total supera un presupuesto semanal de 100 €.
No necesitas hacerlo perfecto. La idea es construir una solución que funcione, probarla y poder explicar tu código.
Entregables individuales
Un archivo mi_gestor_gastos.py.
Una captura o salida de ejemplo del programa funcionando.
Una breve explicación: qué hace el programa, qué concepto le resultó más difícil y cómo lo resolvió.
Un repositorio de GitHub

"""


# ==========================================
# RETO INDIVIDUAL: MI GESTOR DE GASTOS
# ==========================================

# 1. Definición de la lista de gastos (puedes cambiar estos números)
gastos = [12, 8, 25, 15, 30]
presupuesto_maximo = 100

print("--- REPORTE DE GASTOS SEMANALES ---")
print(f"Gastos registrados: {gastos}\n")

# --- FUNCIONES (Requisito Nivel 2 y 3) ---

def calcular_total(lista_gastos):
    """Calcula la suma total de los gastos usando un bucle."""
    suma_total = 0
    for gasto in lista_gastos:
        suma_total += gasto  # Suma cada gasto al total
    return suma_total

# --- CÁLCULOS PRINCIPALES ---

# 1. Calcular el total llamando a la función
total = calcular_total(gastos)
print(f"1. Total de gastos: {total} €")

# 2. Calcular el gasto medio (Evitando error si la lista está vacía - Nivel 3)
if len(gastos) > 0:
    media = total / len(gastos)
    print(f"2. Gasto medio: {media:.2f} €")
else:
    print(f"2. Gasto medio: 0 € (No hay gastos registrados)")

# 3. Mostrar gastos que superan un límite (Nivel 3: Filtro dinámico)
print("\n3. Filtrado de gastos:")
try:
    # Permite al usuario elegir el límite, por defecto sugerimos 20 €
    limite_usuario = input("Introduce el límite para filtrar los gastos (Presiona Enter para usar 20 €): ")
    
    if limite_usuario == "":
        limite = 20.0
    else:
        limite = float(limite_usuario)
except ValueError:
    print("Entrada no válida. Usando límite por defecto de 20 €.")
    limite = 20.0

print(f"Gastos mayores a {limite} €:")
hay_mayores = False
for gasto in gastos:
    if gasto > limite:
        print(f"   - {gasto} €")
        hay_mayores = True

if not hay_mayores:
    print("   No hay gastos que superen ese límite.")

# 4. Comparación con el presupuesto de 100 €
print("\n4. Control de Presupuesto:")
if total > presupuesto_maximo:
    print(f"⚠️ ¡Alerta! Has superado el presupuesto semanal de {presupuesto_maximo} €.")
else:
    print(f"✅ ¡Buen trabajo! Estás dentro del presupuesto semanal de {presupuesto_maximo} €.")

