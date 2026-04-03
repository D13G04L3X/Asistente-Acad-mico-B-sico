import os
from pathlib import Path
from datetime import datetime
from google import genai

MODEL = "gemini-2.5-flash"


SAMPLE_TEXTS = {
    "1": """
Buenas tardes profesor.

No pude asistir a clase porque me encontraba en una cita médica.

Quisiera saber si es posible entregar la actividad mañana.

Gracias.
""",
    "2": """
Buenos días.

No pude presentar el trabajo en la fecha acordada porque tuve una emergencia familiar.

Agradezco si me permite enviarlo con retraso.

Cordial saludo.
""",
    "3": """
La inteligencia artificial aplicada mediante APIs permite automatizar tareas de procesamiento de texto,
integración de servicios y generación de respuestas. Su uso requiere manejo de credenciales, diseño de prompts
y validación de resultados para asegurar calidad y pertinencia.
""",
}


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "No se encontró la variable de entorno GEMINI_API_KEY."
        )
    return genai.Client(api_key=api_key)


def ask_model(client: genai.Client, prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    text = getattr(response, "text", None)
    return text.strip() if text else "No se recibió una respuesta de texto."


def summarize_text(client: genai.Client, text: str) -> str:
    prompt = f"""
Eres un asistente académico.

Resume el siguiente texto en UNA sola oración, clara y precisa.
No agregues información nueva. No expliques el proceso. Responde solo con el resumen.

Texto:
{text}
"""
    return ask_model(client, prompt)


def classify_text(client: genai.Client, text: str) -> str:
    prompt = f"""
Eres un asistente académico.

Clasifica el siguiente mensaje en UNA sola categoría, usando exactamente una de estas opciones:
- solicitud
- excusa
- agradecimiento
- queja
- consulta
- informativo
- otro

Responde solo con la categoría elegida. No agregues explicación.

Texto:
{text}
"""
    return ask_model(client, prompt)


def formal_reply(client: genai.Client, text: str) -> str:
    prompt = f"""
Eres un asistente académico.

Redacta una respuesta formal, breve, respetuosa y coherente para el siguiente mensaje.
Extensión sugerida: 3 a 5 líneas.
No uses listas. No expliques el proceso. Solo escribe la respuesta.

Mensaje:
{text}
"""
    return ask_model(client, prompt)


def get_user_text() -> str:
    print("\n=== Asistente Académico Básico ===")
    print("1. Usar texto de solicitud académica")
    print("2. Usar texto de excusa")
    print("3. Usar texto informativo")
    print("4. Escribir mi propio texto")

    option = input("\nElige una opción (1-4): ").strip()

    if option in SAMPLE_TEXTS:
        return SAMPLE_TEXTS[option].strip()

    print("\nEscribe tu texto. Finaliza con una línea vacía:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def save_results(original: str, summary: str, classification: str, reply: str) -> Path:
    output_dir = Path("4. Análisis crítico")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"resultado_asistente_{timestamp}.txt"

    content = f"""ASISTENTE ACADÉMICO BÁSICO
Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

TEXTO ORIGINAL:
{original}

RESUMEN:
{summary}

CLASIFICACIÓN:
{classification}

RESPUESTA FORMAL:
{reply}
"""

    output_file.write_text(content, encoding="utf-8")
    return output_file


def main():
    try:
        client = get_client()
        user_text = get_user_text()

        if not user_text:
            print("No ingresaste texto. El programa finalizó.")
            return

        summary = summarize_text(client, user_text)
        classification = classify_text(client, user_text)
        reply = formal_reply(client, user_text)

        print("\n" + "=" * 60)
        print("RESUMEN:")
        print(summary)

        print("\nCLASIFICACIÓN:")
        print(classification)

        print("\nRESPUESTA FORMAL:")
        print(reply)
        print("=" * 60)

        saved_file = save_results(user_text, summary, classification, reply)
        print(f"\nResultados guardados en: {saved_file}")

    except Exception as e:
        print(f"\nOcurrió un error: {e}")


if __name__ == "__main__":
    main()