from app.ollama_service import construir_prompt, generar_busquedas, ollama_disponible
from app.paths import get_palabras_path
from app.search_terms import guardar_busquedas_desde_linea, palabras_txt_existe

ARCHIVO_SALIDA = get_palabras_path()


if __name__ == "__main__":
    palabra_usuario = input("\n📝 Introduce una palabra o frase clave: ")
    generar_busquedas(palabra_usuario)
