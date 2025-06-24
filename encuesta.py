import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV (verificá que el archivo esté en la misma carpeta)
df = pd.read_csv("encuesta.csv")

# Asegurar que la columna EDAD sea numérica
df["EDAD"] = pd.to_numeric(df["EDAD"], errors='coerce')

# -------------------------
# 1. Rango y Promedio de Edad
# -------------------------
print("RANGO DE EDAD")
print("Edad mínima:", df["EDAD"].min())
print("Edad máxima:", df["EDAD"].max())
print("Promedio de edad:", round(df["EDAD"].mean(), 2))

# -------------------------
# 2. Interés en Política
# -------------------------
col_politica = "¿Te intereasa la politica?  -Mucho -Poco -Nada"
interes = df[col_politica].value_counts()

print("\n INTERÉS EN POLÍTICA")
print(interes)

# Gráfico
interes.plot(kind='bar', color='skyblue')
plt.title("Nivel de interés en política")
plt.xlabel("Respuesta")
plt.ylabel("Cantidad de personas")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -------------------------
# 3. Opiniones sobre Política
# -------------------------
col_opinion = "¿Por qué te interesa o no te interesa la politica? -Me aburre -No entiendo como funciona -Me preocupa el futuro - Me gusta debatir y estar informado"

opciones = {
    "Me aburre": "aburre",
    "No entiendo cómo funciona": "no entiendo",
    "Me preocupa el futuro": "preocupa el futuro",
    "Me gusta debatir": "debatir"
}

print("\n OPINIONES SOBRE POLÍTICA")
for desc, palabra in opciones.items():
    cantidad = df[col_opinion].str.contains(palabra, case=False, na=False).sum()
    print(f"{desc}: {cantidad}")

# -------------------------
# 4. Temas de Interés
# -------------------------
col_temas = "¿Qué temas te interesan de la política? -Educación -Economía -Inclusión -Tecnología -Otros"
temas = ["Educación", "Economía", "Inclusión", "Tecnología", "Otros"]
valores = [df[col_temas].str.contains(t, case=False, na=False).sum() for t in temas]

# Mostrar
print("\n TEMAS DE INTERÉS")
for t, v in zip(temas, valores):
    print(f"{t}: {v}")

# Gráfico
plt.bar(temas, valores, color="mediumseagreen")
plt.title("Temas de interés político")
plt.ylabel("Cantidad de personas")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
