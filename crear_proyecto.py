import os

directorios = [
    "src/core",
    "src/ui",
    "tests",
    "docs"
]

archivos = {
    "src/core/__init__.py": "",
    "src/core/fisicas.py": "# Aquí irán las ecuaciones del Centro de Gravedad\n",
    "src/ui/__init__.py": "",
    "src/ui/graficos.py": "# Aquí irán los gráficos de la envolvente de vuelo\n",
    "src/main.py": "# Este es el orquestador principal del programa\n",
    "requirements.txt": "numpy\nmatplotlib\n",
    "README.md": "# Simulador de Peso y Balance\n",
    ".gitignore": "__pycache__/\n*.pyc\nvenv/\n"
}

for d in directorios:
    os.makedirs(d, exist_ok=True)

for ruta, contenido in archivos.items():
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

print("¡Estructura base generada con éxito!")