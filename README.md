# Asistente-Acad-mico-B-sico
Uso de una API Gratuita de Inteligencia Artificial para la Construcción de un Asistente Académico Básico

📘 Asistente Académico Básico con API de Google Gemini
Curso

Herramientas de Inteligencia Artificial
Institución Universitaria ITM
Año: 2026

📌 Descripción del Proyecto

Este proyecto consiste en la construcción de un asistente académico básico desarrollado en Python que se conecta a la API de Google Gemini mediante autenticación con clave API.

El sistema permite:

📄 Resumir un mensaje académico en una sola oración.
🏷️ Clasificar el mensaje según su intención.
✍️ Redactar una respuesta formal y respetuosa.

El objetivo es comprender cómo consumir una API de inteligencia artificial de forma programática, estructurar prompts correctamente y analizar la calidad de los resultados obtenidos.

🎯 Objetivo General

Desarrollar un asistente académico básico mediante el consumo de una API gratuita de inteligencia artificial, aplicando conceptos de integración tecnológica, diseño de prompts y análisis crítico de resultados.

🛠 Tecnologías Utilizadas
Python 3.10 o superior
Librería oficial google-genai
API de Google Gemini
Entorno virtual (venv)

🚀 INSTRUCTIVO DE INSTALACIÓN Y EJECUCIÓN
🔹 PASO 1 – Verificar instalación de Python

En la terminal o CMD:

python --version

Debe aparecer algo como:

Python 3.11.x

Si no está instalado, descargar desde:
https://www.python.org/downloads/

🔹 PASO 2 – Crear entorno virtual

Ubícate en la carpeta del proyecto:

cd "E:\Universidad\ITM\Materias\Ingeniería de Sistemas\3. Herramientas de Inteligencia Artificial\Entregables\Entrega 2\API_Google\Asistente-Académico-Básico"

Crear entorno virtual:

python -m venv venv

Activarlo:

En Windows:

venv\Scripts\activate

Si se activó correctamente verás:

(venv) C:\...
🔹 PASO 3 – Instalar dependencias

Con el entorno activo:

pip install google-genai

Verificar instalación:

pip list

Debe aparecer:

google-genai
🔹 PASO 4 – Configurar la API Key

Debes generar tu API Key en Google AI Studio.

Luego configurar la variable de entorno:

En Windows (CMD):
set GEMINI_API_KEY=TU_CLAVE_AQUI
En PowerShell:
$env:GEMINI_API_KEY="TU_CLAVE_AQUI"

⚠️ Importante:

No subir la API Key a GitHub.
No escribirla directamente en el código.
No compartirla públicamente.
🔹 PASO 5 – Ejecutar el programa

Desde la raíz del proyecto:

python "2. Código/API_Google.py"

El sistema mostrará un menú con opciones:

1. Solicitud académica
2. Excusa
3. Texto informativo
4. Escribir mi propio texto

Luego generará:

Resumen
Clasificación
Respuesta formal

Y guardará automáticamente los resultados en:

4. Análisis crítico/