# mi_gestor_gastos



# Mi Gestor de Gastos Semanales 💰

Este es un programa sencillo en Python diseñado para ayudar a los usuarios a registrar, controlar y analizar sus gastos semanales frente a un presupuesto establecido.

## 🚀 ¿Qué hace el programa?
El script `mi_gestor_gastos.py` realiza las siguientes funciones:
* **Almacenamiento:** Guarda los gastos de la semana en una lista.
* **Cálculo Total:** Suma todos los gastos acumulados mediante una función optimizada.
* **Promedio Semanal:** Calcula el gasto medio por día/artículo.
* **Control de Presupuesto:** Compara el total con un límite de 100 € y genera una alerta visual si se supera.
* **Filtro Avanzado:** Permite al usuario introducir un límite personalizado en la consola para ver qué gastos superaron esa cantidad.

## 🧠 Desafíos y Aprendizaje
* **Lo más difícil:** Gestionar la lógica para evitar errores críticos en el sistema.
* **Cómo se resolvió:** Al implementar el cálculo de la media, existía el riesgo de que una lista vacía provocara un error de división por cero (`ZeroDivisionError`). Lo solucioné añadiendo una estructura condicional `if len(gastos) > 0:` que verifica que existan datos antes de operar, garantizando la estabilidad del programa.

## 🛠️ Cómo ejecutarlo
1. Asegúrate de tener instalado Python 3.
2. Clona o descarga este repositorio.
3. Ejecuta el archivo desde tu terminal:
   ```bash
   python mi_gestor_gastos.py
   ```
