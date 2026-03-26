import os
from google import genai

# Configurar la clave API en una variable de entorno antes de ejecutar:
# En Windows (PowerShell):
# $env:GEMINI_API_KEY="tu_clave"
#
# En Windows (CMD):
# set GEMINI_API_KEY=tu_clave

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la variable GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

modelo = "gemini-2.5-flash"