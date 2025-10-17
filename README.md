# Lyrics Eater (Financiado por FondoCyt)

Herramienta profesional para extraer letras de canciones desde Genius.com y enlaces de videos de YouTube automáticamente.

## ¿Qué es Lyrics Eater?

Lyrics Eater es una aplicación de Python que busca canciones en Genius.com, extrae sus letras y encuentra los videos musicales correspondientes en YouTube, guardando toda la información en un archivo Excel organizado.

## Características

- 🔍 **Búsqueda automática** de canciones en Genius
- 📝 **Extracción de metadata**: artista, álbum, género, sello discográfico
- 🎵 **Scraping de letras** completas
- 🎬 **Enlaces de YouTube** para cada canción (opcional)
- 📊 **Exportación a Excel** con formato profesional
- 📦 **Procesamiento por lotes** desde archivo de texto
- ⚡ **Manejo robusto de errores** y timeouts

## Estructura del Proyecto

```
lyrics-eater/
├── src/                    # Código fuente
│   ├── clients/           # Clientes de APIs (Genius, YouTube)
│   ├── services/          # Lógica de procesamiento
│   ├── models/            # Modelos de datos
│   └── utils/             # Utilidades (config, archivos)
├── main.py                # Punto de entrada
├── .env                   # Variables de entorno
├── searches.txt           # Búsquedas (una por línea)
└── requirements.txt       # Dependencias
```

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repo>
   cd lyrics-eater
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar token de Genius**
   
   - Ve a https://genius.com/api-clients
   - Crea una aplicación y copia el "Client Access Token"
   
   Crea un archivo `.env` con:
   ```env
   GENIUS_ACCESS_TOKEN=tu_token_de_genius_aquí
   ```
   
   > **Nota:** Los enlaces de YouTube se obtienen automáticamente mediante scraping, ¡sin necesidad de API key!

4. **Crear archivo de búsquedas**
   
   Edita `searches.txt` con las canciones que deseas buscar (una por línea):
   ```
   Obsesión - Aventura
   Propuesta Indecente - Romeo Santos
   Bachata Rosa - Juan Luis Guerra
   ```

## Uso

### Ejecución básica
```bash
python main.py
```

### Resultado

El programa generará un archivo `genius_songs.xlsx` con las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| **genero** | Géneros musicales de la canción |
| **artista** | Nombre del artista |
| **cancion** | Título de la canción |
| **letras** | Letras completas de la canción |
| **enlace_genius** | URL de Genius.com |
| **enlace_youtube** | URL del video en YouTube (obtenido por scraping) |
| **discografica** | Sello discográfico/label |

### Formato del archivo searches.txt

```txt
# Puedes agregar comentarios con #
# Una búsqueda por línea

Obsesión - Aventura
Propuesta Indecente - Romeo Santos
Imagine - John Lennon

# Las líneas vacías se ignoran
Bohemian Rhapsody - Queen
```

## Configuración Avanzada

Puedes modificar la configuración en `src/utils/config.py`:

```python
API_TIMEOUT = 20              # Timeout para búsquedas (segundos)
SCRAPING_TIMEOUT = 20         # Timeout para extracción de letras
RESULTS_PER_PAGE = 1          # Resultados por búsqueda (1 = primer resultado)
OUTPUT_FILE = "genius_songs.xlsx"  # Nombre del archivo de salida
```

## 🛠️ Dependencias

- `requests`: Para peticiones HTTP
- `beautifulsoup4`: Para scraping de letras
- `pandas`: Para manejo de datos
- `openpyxl`: Para exportar a Excel
- `python-dotenv`: Para variables de entorno

