
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datos/ventas.csv")

ventas_totales = df["sales_amount"].sum()

venta_maxima = df["sales_amount"].max()

venta_minima = df["sales_amount"].min()

print("Ventas totales:", ventas_totales)
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)

plt.figure(figsize=(12,5))

df_filtrado = df.head(30)

plt.plot(
    df_filtrado["sales_date"],
    df_filtrado["sales_amount"],
    marker="o"
)

plt.title("Evolución de ventas")
plt.xlabel("Fecha")
plt.ylabel("Monto de ventas")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../resultados/grafico_ventas.png")

print("Gráfico generado correctamente")
