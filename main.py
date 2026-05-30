from generador import generar_busquedas
import script


def main():
    palabra_usuario = input("\n📝 Introduce una palabra o frase clave: ")
    generar_busquedas(palabra_usuario)
    print("\nIniciando el script de automatización (listener). Pulsa la tecla configurada para activar...")
    script.start_listener()


if __name__ == "__main__":
    main()
