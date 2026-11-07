<div align="center">

# 🩺 Diabetes Prediction with Deployment

**Sistema de predicción de diabetes basado en Machine Learning, con interfaces web en Flask y Streamlit.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://d-pred.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

## 📌 Descripción

**Diabetes Prediction with Deployment** es un proyecto *end-to-end* de aprendizaje automático que clasifica a una persona como **diabética** o **no diabética** a partir de variables clínicas y demográficas.

El modelo fue entrenado mediante **Regresión Logística** y se expone a través de dos alternativas de aplicación web:

- **Flask:** interfaz tradicional basada en HTML y Jinja2.
- **Streamlit:** interfaz interactiva, ligera y orientada a prototipado rápido.

> ⚠️ **Aviso:** Este proyecto tiene fines educativos y de demostración. No debe utilizarse como herramienta de diagnóstico médico ni sustituir la evaluación de un profesional de la salud.

## 🧠 Flujo del proyecto

```text
Dataset → Preprocesamiento → Escalado de variables → Entrenamiento
        → Serialización del modelo → API / Interfaz web → Predicción
```

El flujo incluye:

1. Carga y exploración del dataset.
2. Limpieza y preparación de los datos.
3. Escalado de características con `StandardScaler`.
4. Entrenamiento de un modelo de **Regresión Logística**.
5. Serialización del escalador y del modelo mediante `pickle`.
6. Inferencia desde una aplicación Flask o Streamlit.

## 🏗️ Arquitectura

| Componente | Tecnología | Función |
|---|---|---|
| Modelo de Machine Learning | `scikit-learn` | Clasificación binaria: diabético / no diabético |
| Algoritmo principal | Regresión Logística | Estimación de la probabilidad de diabetes |
| Preprocesamiento | `StandardScaler` | Estandarización de variables numéricas |
| Serialización | `pickle` | Persistencia del modelo y del escalador |
| Backend | Flask | Servidor web y lógica de predicción |
| Frontend alternativo | Streamlit | Interfaz interactiva de usuario |
| Notebook | Jupyter Notebook | Desarrollo, análisis y entrenamiento del modelo |

## 📁 Estructura del repositorio

```text
Diabetes-Prediction-With-Deployment/
│
├── dataset/
│   └── # Dataset utilizado para el entrenamiento
│
├── Model/
│   ├── standardScalar.pkl
│   └── modelForPrediction.pkl
│
├── notebook/
│   └── Logistic_Regression.ipynb
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── single_prediction.html
│
├── app.py
├── app1.py
├── requirements.txt
└── README.md
```

## 🚀 Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone [https://github.com/hardikjp7/Diabetes-Prediction-With-Deployment.git](https://github.com/hardikjp7/Diabetes-Prediction-With-Deployment.git)
cd Diabetes-Prediction-With-Deployment
```

### 2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

En Linux o macOS:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🖥️ Ejecución de la aplicación

### Opción 1: Flask

```bash
python app.py
```

Luego abre en el navegador la URL local mostrada en la terminal, normalmente:

```text
http://127.0.0.1:5000/
```

### Opción 2: Streamlit

```bash
streamlit run app1.py
```

La aplicación se abrirá automáticamente o podrás acceder mediante la URL local indicada por Streamlit.

## 🧪 Uso de la aplicación

1. Ingresa los valores solicitados en el formulario.
2. Presiona el botón **Predict**.
3. El modelo procesa los datos y devuelve una predicción.
4. El resultado indica si la persona fue clasificada como diabética o no diabética.

Los datos ingresados son escalados con el mismo `StandardScaler` utilizado durante el entrenamiento, garantizando consistencia entre el entrenamiento y la inferencia.

## 📊 Modelo

| Elemento | Detalle |
|---|---|
| Tipo de problema | Clasificación binaria |
| Variable objetivo | Diabético / No diabético |
| Algoritmo | Regresión Logística |
| Preprocesamiento | `StandardScaler` |
| Persistencia | `pickle` |
| Archivo del modelo | `Model/modelForPrediction.pkl` |
| Archivo del escalador | `Model/standardScalar.pkl` |

## 📓 Notebook

El notebook [`Logistic_Regression.ipynb`](./notebook/Logistic_Regression.ipynb) contiene:

- Análisis exploratorio de datos.
- Preparación y escalado de variables.
- Entrenamiento del modelo.
- Evaluación del rendimiento.
- Serialización del modelo y del preprocesador.

## ☁️ Despliegue

### Streamlit Community Cloud

La aplicación puede desplegarse directamente en [Streamlit Community Cloud](https://streamlit.io/cloud).

1. Sube el repositorio a GitHub.
2. Ingresa a Streamlit Community Cloud.
3. Selecciona el repositorio y el archivo `app1.py`.
4. Configura la versión de Python y las dependencias.
5. Despliega la aplicación.

El badge superior enlaza a la aplicación desplegada en Streamlit. Streamlit recomienda insertar ese badge en el `README.md` una vez que la aplicación está publicada. [2]

### Flask

Para producción, Flask puede ejecutarse mediante un servidor WSGI como **Gunicorn**:

```bash
pip install gunicorn
gunicorn app:app
```

Dependiendo del proveedor de hosting, pueden requerirse configuraciones adicionales relacionadas con puertos, variables de entorno, archivos estáticos y procesos.

## 🛠️ Posibles mejoras

- Agregar pruebas unitarias e integración.
- Implementar validación de datos de entrada.
- Incluir métricas como precisión, recall, F1-score y matriz de confusión.
- Comparar otros algoritmos: Random Forest, XGBoost, SVM o redes neuronales.
- Agregar Docker para un despliegue reproducible.
- Implementar CI/CD con GitHub Actions.
- Incluir explicabilidad del modelo con SHAP o LIME.
- Mejorar la interfaz con visualizaciones y retroalimentación al usuario.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para proponer cambios:

1. Haz un *fork* del repositorio.
2. Crea una rama nueva:

```bash
git checkout -b feature/nueva-funcionalidad
```

3. Realiza los cambios y confirma los archivos:

```bash
git add .
git commit -m "feat: agregar nueva funcionalidad"
git push origin feature/nueva-funcionalidad
```

4. Abre un *Pull Request*.

## 📄 Licencia

Este proyecto se distribuye con fines educativos. Revisa la licencia del repositorio antes de reutilizar el código o los datos.

---

<div align="center">

**Desarrollado con Python, scikit-learn, Flask y Streamlit.**

</div>
