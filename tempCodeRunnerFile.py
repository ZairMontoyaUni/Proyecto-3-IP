
import cupicharts as c

##### Funciones auxiliares (NO MODIFICAR):

def mostrar_cancion(cancion: dict) -> None:
    """
    Muestra la información de una canción en Cupicharts.

    Parámetros:
        cancion (dict): Diccionario con la información de la canción.
    """
    if cancion is not None and cancion != {}:
        print("\n")
        print("#" * 50)
        
        print((
            "Título: {}\n"
            "Fecha en el top: {}\n"
            "Artista: {}\n"
            "Posición máxima: {}\n"
            "Semanas en el top: {}\n"
            "Álbum: {}\n"
            "Fecha de lanzamiento: {}\n"
            "Popularidad: {}\n"
            "Explícita: {}\n"
            "Número de oyentes: {}\n"
            "Número de reproducciones: {}\n"
            "Duración: {}\n"
        ).format(
            cancion["title"], cancion["chart_week"],
            cancion["performer"], cancion["peak_pos"],
            cancion["wks_on_chart"], cancion["album_name"],
            cancion["release_date"], cancion["popularity"],
            cancion["explicit"], cancion["listeners"],
            cancion["play_count"], cancion["duration_s"]
        ))
        print("#" * 50)
    else:
        print("Error: Diccionario de canción inválido.")
    
def mostrar_canciones(canciones: list) -> None:
    """
    Muestra la información de una lista de canciones en Cupicharts.

    Parámetros:
        canciones (list): Lista de diccionarios con la información de las canciones.
    """
    if canciones is not None and canciones != []:
        print("\n Canciones en Cupicharts:")
        print("-" * 50)
        
        for cancion in canciones:
            mostrar_cancion(cancion)
        
        print("-" * 50)
    else:
        print("Error: Lista de canciones inválida.")
        
def mostrar_canciones_en_album(canciones: list) -> None:
    """
    Muestra los títulos de las canciones en un álbum específico.

    Parámetros:
        canciones (list): Lista con los títulos de las canciones del álbum.
    """
    if canciones is not None and canciones != []:
        print("\n Canciones en el álbum:")
        print("-" * 50)
    
        for cancion in canciones:
            print(cancion)
            
        print("-" * 50)
    else:
        print("Error: Lista de canciones inválida.")
##### Fin de funciones auxiliares



# Funciones a implementar (solo aquellas con TODOs):

# Función 2:
def ejecutar_buscar_canciones_por_artista_popularidad(cupicharts: dict) -> None:
    """
    Ejecuta la búsqueda de las canciones de un artista con un rango de popularidad específico.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
    
    Se debe pedir al usuario el nombre del artista y un rango de popularidad (mínima y máxima).
    