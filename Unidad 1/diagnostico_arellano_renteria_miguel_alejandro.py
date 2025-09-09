# Simulador de pedidos
# Conceptos básicos: variables, inputs, condicionales, funciones y bucles

# Temática: Papelería creativa
productos = ["colores", "post-it", "reglas"]
precios = [35, 18, 22]

# Función para calcular el total
def calcular_total(cantidad, precios):
    total = 0
    for i in range(len(cantidad)):
        total += cantidad[i] * precios[i]
    return total

# Menú para el usuario
print("🛍️ Bienvenido al menú de papelería")
nombre = input("Ingresa tu nombre: ")
cantidad = []

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_agregar = int(input(f"¿Cuántos {productos[i]} desea? "))
    cantidad.append(cantidad_agregar)

# Mostrar resumen de compra
total = calcular_total(cantidad, precios)

print(f"\nHola {nombre}, compraste:")
for i in range(len(productos)):
    if cantidad[i] > 0:
        print(f"- {cantidad[i]} {productos[i]} (${cantidad[i] * precios[i]})")

print(f"\nTotal a pagar: ${total}")