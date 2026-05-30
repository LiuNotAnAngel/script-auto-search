import ollama

# --- CONFIGURACIÓN ---
MODELO = "novaforgeai/gemma2:2b-optimized" 

# El archivo de salida donde se guardarán los resultados
ARCHIVO_SALIDA = "palabras.txt"

# --- PROMPT (La instrucción que le damos al modelo) ---
def construir_prompt(palabra_clave):
    """
    Construye un prompt efectivo para generar términos de búsqueda
    """
    prompt = f"""
Eres un asistente que genera términos de búsqueda. Tu tarea es crear una lista de 30 términos de búsqueda variados, creativos y útiles para la palabra clave: '{palabra_clave}'.

Instrucciones:
- Genera búsquedas que exploren diferentes ángulos: noticias, contexto histórico, análisis, controversias, etc.
- Formatea la respuesta como una lista, con un término por línea
- Asegúrate de incluir la palabra clave original en la mayoría de las búsquedas.
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

# --- FUNCIÓN PRINCIPAL ---
def generar_busquedas(palabra_clave):
    """Envía la palabra clave al modelo y guarda los resultados en un archivo"""
    if not palabra_clave or palabra_clave.strip() == "":
        print("❌ Error: No has introducido ninguna palabra clave.")
        return

    print(f"🧠 Procesando la palabra clave: '{palabra_clave}' con el modelo {MODELO}...")
    try:
        # Llamamos a Ollama con nuestro prompt
        respuesta = ollama.generate(
            model=MODELO,
            prompt=construir_prompt(palabra_clave)
        )

        # Extraemos el texto que generó el modelo
        busquedas_generadas = respuesta['response'].strip()

        # Guardamos el resultado en el archivo .txt
        with open(ARCHIVO_SALIDA, 'w', encoding='utf-8') as archivo:
            archivo.write(f"Palabra clave: {palabra_clave}\n")
            archivo.write(f"{'-'*30}\n")
            archivo.write(busquedas_generadas)
            archivo.write(f"\n{'-'*30}\n")
            archivo.write("Proceso completado con éxito.")

        print("\n--- Resultado generado ---")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# --- PUNTO DE ENTRADA DEL PROGRAMA ---
if __name__ == "__main__":
    # Le pedimos la palabra clave al usuario
    palabra_usuario = input("\n📝 Introduce una palabra o frase clave: ")
    generar_busquedas(palabra_usuario)