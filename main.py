from generador import generar_busquedas, ollama_disponible
import script


def main():
    palabra_usuario = input("\n📝 Introduce una palabra o frase clave: ")
    if ollama_disponible():
        generar_busquedas(palabra_usuario)
    else:
        print("\nOllama no está disponible. Se usará palabras.txt existente sin generar nuevas búsquedas.")
    print("\nIniciando el script de automatización (listener). Pulsa la tecla configurada para activar...")
    script.start_listener()


if __name__ == "__main__":
    main()
