import os
import papermill as pm

# Lista de notebooks en orden (dentro de la carpeta notebooks/)
notebooks = [
    "00_setup_importacion.ipynb",
    "01_exploracion_datos.ipynb",
    "02_modelo_demanda_divisas.ipynb",
    "03_modelo_tipo_de_cambio.ipynb",
    "04_optimizar_compra_divisas.ipynb",
    "05_simulacion_backtesting.ipynb",
    "06_dashboard_resultados.ipynb",
    "07_informe_presentacion.ipynb"
]

output_dir = "executed"

# Crear carpeta de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Ejecutar cada notebook y guardar versión ejecutada
for nb in notebooks:
    entrada = f"notebooks/{nb}"
    salida = os.path.join(output_dir, nb)
    print(f"▶ Ejecutando: {entrada}")
    pm.execute_notebook(input_path=entrada, output_path=salida)
    print(f"✅ Guardado en: {salida}")