import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. DATOS (como si fuera Excel)
# -----------------------------
data = {
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"],
    "precio": [2500, 80, 150, 1200, 200],
    "cantidad": [3, 10, 7, 4, 15]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. PROCESAMIENTO CON NUMPY
# -----------------------------
df["total"] = np.multiply(df["precio"], df["cantidad"])

# descuento si supera 3000
df["descuento"] = np.where(df["total"] > 3000, df["total"] * 0.10, 0)

df["total_final"] = df["total"] - df["descuento"]

# -----------------------------
# 3. MOSTRAR TABLA
# -----------------------------
print("\n📦 VENTAS:")
print(df)

print("\n📊 RESUMEN:")
print("Total vendido:", np.sum(df["total_final"]))
print("Promedio:", np.mean(df["total_final"]))
print("Máximo:", np.max(df["total_final"]))

# -----------------------------
# 4. GRÁFICO CON MATPLOTLIB
# -----------------------------
plt.figure(figsize=(9,5))

plt.bar(df["producto"], df["total_final"])

plt.title("Ventas finales por producto")
plt.xlabel("Producto")
plt.ylabel("Ingresos")

plt.xticks(rotation=30)

plt.show()