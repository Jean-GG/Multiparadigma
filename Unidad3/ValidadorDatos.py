import re # re se utiliza para trabajar con expresiones regulares, de esta forma se puede validar ciertos patrones en cadenas

def validar_esquema(url: str) -> bool: # Valida que la URL comience con 'http://' o 'https://'.
    return url.startswith("http://") or url.startswith("https://")

def validar_dominio(url: str) -> bool: #Extrae y valida la parte del dominio de la URL
    # Si la URL tiene un esquema, se elimina para analizar solo el dominio
    if validar_esquema(url):
        sin_esquema = url.split("://", 1)[1]
    else:
        sin_esquema = url
    # Se toma la parte antes de la primera '/' (En dado caso de que existe)
    dominio = sin_esquema.split("/", 1)[0]
    return '.' in dominio and not dominio.startswith('.') and not dominio.endswith('.')

def validar_caracteres(url: str) -> bool: # Valida que la URL contenga unicamente caracteres permitidos.
    # Patron simplificado que valida la estructura de caracteres permitidos en una URL.
    patron = r'^[A-Za-z0-9:/?#[\]@!$&\'()*+,;=._%-~]+$'
    return bool(re.match(patron, url))

# Ejemplos de uso
if __name__ == "__main__":
    urls = (
        "https://www.ejemploBueno.com/path?query=777",
        "http://sub.dominio.mx",
        "ftp://ejemploMalo.com",                   # Esquema inválido
        "https://juegos_gratis",              # Dominio sin punto
        "https://www.TEC.com/carreras especialidades",  # Caracteres no permitidos (en este caso seran los espacios)
    )
    
    for url in urls:
        esquema_valido = validar_esquema(url)
        dominio_valido = validar_dominio(url)
        caracteres_validos = validar_caracteres(url)
        url_valida = esquema_valido and dominio_valido and caracteres_validos
        
        print("URL:", url)
        print("  Esquema valido:", esquema_valido)
        print("  Dominio valido:", dominio_valido)
        print("  Caracteres validos:", caracteres_validos)
        print("  URL valida:", url_valida)
        print("-" * 40)
