from generador import (
    generar_busquedas,
    guardar_busquedas_desde_linea,
    ollama_disponible,
    palabras_txt_existe,
)
import script


def main():
    if ollama_disponible():
        palabra_usuario = input("\n📝 Introduce una palabra o frase clave: ")
        generar_busquedas(palabra_usuario)
    else:
        print("\nOllama no está disponible.")
        linea_usuario = input(
            "📝 Introduce terminos separados por comas: "
        )
        cantidad = guardar_busquedas_desde_linea(linea_usuario)

        if cantidad > 0:
            print(f"\nSe guardaron {cantidad} terminos en palabras.txt.")
        elif palabras_txt_existe():
            print("\nEntrada invalida. Se usará palabras.txt existente.")
        else:
            print("\nEntrada invalida y no existe palabras.txt. No se iniciará la automatización.")
            return
        
    print(f"\nIniciando el script de automatización. Pulsa la tecla {script.TECLA_ACTIVACION} para activar...")
    script.start_listener()


if __name__ == "__main__":
    main()
