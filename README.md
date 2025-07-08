# Rah-Jos-Jac-Proyecto-fin-de-curso
#  ESTO ES UNA PRUEBA 


# Sistema de Predicción y Optimización de Compras de Divisas
![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange?logo=jupyter)
![Estado](https://img.shields.io/badge/estado-en_desarrollo-yellow)
![Estado](https://img.shields.io/badge/🛠️_proyecto-en_desarrollo-blue)
![Fase](https://img.shields.io/badge/fase-piloto-orange)

Este proyecto desarrolla un sistema para anticipar la demanda de divisas y la evolución del tipo de cambio, con el fin de optimizar las decisiones de compra en una empresa de cambio de moneda.

## Objetivos

- Predecir la cantidad de cada divisa que se requerirá en los próximos días/semanas  
- Estimar el tipo de cambio futuro entre divisas clave  
- Sugerir cuándo y cuánto comprar para maximizar rentabilidad  
- Simular estrategias pasadas para cuantificar impacto (backtesting)

---

## Estructura del repositorio

```bash
notebooks/
├── 00_setup_importacion.ipynb
├── 01_exploracion_datos.ipynb
├── 02_modelo_demanda_divisas.ipynb
├── 03_modelo_tipo_de_cambio.ipynb
├── 04_optimizar_compra_divisas.ipynb
├── 05_simulacion_backtesting.ipynb
├── 06_dashboard_resultados.ipynb
├── 07_informe_presentacion.ipynb

data/              → Datos crudos y limpios (CSV, Excel, etc.)
reports/           → Predicciones, resultados, gráficas, dashboards
executed/          → Cuadernos ejecutados con resultados visibles
scripts/           → Código para descargas automáticas y utilidades
src/               → Funciones auxiliares reutilizables (opcional)
launcher.py        → Lanza todos los notebooks en orden con papermill
requirements.txt   → Librerías necesarias
README.md          → Este archivo
```



## 🧭 Diagrama del flujo del sistema

![Flujo del sistema](reports/diagrama_flujo_sistema.png)



---

## ¿Cómo ejecutar el proyecto?

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt



