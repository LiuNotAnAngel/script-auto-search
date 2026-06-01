import urllib.error
import urllib.request

import ollama

from .config import MODELO_OLLAMA, OLLAMA_TAGS_URL, TERMINOS_DE_BUSQUEDA
from .paths import get_palabras_path


def ollama_disponible():
    try:
        with urllib.request.urlopen(OLLAMA_TAGS_URL, timeout=2) as response:
            return response.status == 200
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError):
        return False


def construir_prompt(palabra_clave):
    prompt = f"""
Eres un asistente que genera términos de búsqueda. Tu tarea es crear una lista de {TERMINOS_DE_BUSQUEDA} términos de búsqueda variados, creativos y útiles para la palabra clave: '{palabra_clave}'.

Instrucciones:
- Genera búsquedas que exploren diferentes ángulos: noticias, contexto histórico, análisis, controversias, etc.
- Formatea la respuesta como una lista, con un término por línea
- No hace falta incluir la palabra clave original cada vez en los términos generados, pero han de ser relevantes.
- Sé conciso y directo. No des explicaciones adicionales.
- Solo debes generar términos de búsqueda, y nada más.
Ejemplo:
Palabra clave: 'energía renovable'
Respuesta esperada:
- energía renovable avances 2025
- energías renovables en el mundo
- paneles solares vs energía eólica
- futuro de las energías limpias
- impacto económico de las renovables
- energía renovable para el hogar
- comparativa de energías renovables

Ahora, genera la lista para la palabra clave: '{palabra_clave}'
"""
    return prompt


def generar_busquedas(palabra_clave):
    """Envía la palabra clave al modelo y guarda los resultados en un archivo."""
    if not palabra_clave or palabra_clave.strip() == "":
        print("❌ Error: No has introducido ninguna palabra clave.")
        return

    print(f"🧠 Procesando la palabra clave: '{palabra_clave}' con el modelo {MODELO_OLLAMA}...")
    try:
        respuesta = ollama.generate(
            model=MODELO_OLLAMA,
            prompt=construir_prompt(palabra_clave),
        )
        busquedas_generadas = respuesta["response"].strip()

        with open(get_palabras_path(), "w", encoding="utf-8") as archivo:
            archivo.write(busquedas_generadas)

        print("\n--- Resultado generado ---")
    except Exception as exc:
        print(f"Ocurrió un error: {exc}")
