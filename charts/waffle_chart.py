import plotly.express as px
import numpy as np 
import pandas as pd 
import matplotlib as mpl #
import matplotlib.pyplot as plt #
import seaborn as sns
from pywaffle import Waffle
from data.waffle_data import top100_revenue_movies

def create_waffle():
    genre_revenue_table = top100_revenue_movies.groupby('genre')['revenue'].sum().reset_index(name="revenue")

    genre_values = dict(zip(genre_revenue_table['genre'], genre_revenue_table['revenue']))
    proportion = round((100 / sum(genre_revenue_table['revenue'])) * genre_revenue_table['revenue'])

    genre_proportions = dict(zip(genre_revenue_table['genre'], proportion))

    waffle = plt.figure(
        FigureClass= Waffle,
        rows = 10,
        values = genre_proportions,
        legend = {
            'loc': 'upper left',
            'bbox_to_anchor': (1, 1)
        },
        colors = sns.color_palette("Paired", n_colors=len(genre_values)).as_hex(),
        block_arranging_style = 'snake',
        figsize=(10,6),
        block_aspect_ratio = 1,
        dpi = 100,
    )

    plt.tight_layout

    # --- Paso para generar HTML: Guardar como imagen y retornar la etiqueta HTML ---
    # 1. Guarda el gráfico como una imagen temporal. Puedes usar SVG para escalabilidad o PNG.
    image_path = 'waffle_chart.png' # o 'waffle_chart.svg'
    plt.savefig(image_path, bbox_inches='tight') # bbox_inches='tight' recorta el espacio en blanco
    plt.close(waffle) # Cierra la figura para liberar memoria

    # 2. Lee la imagen y codifícala en Base64 para incrustarla directamente en el HTML
    # Esto evita tener que servir el archivo de imagen por separado.
    import base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Determina el tipo MIME de la imagen
    mime_type = "image/png" # o "image/svg+xml" si guardaste como SVG

    # Retorna el string HTML con la imagen incrustada
    html_output = f'<img src="data:{mime_type};base64,{encoded_string}" alt="Waffle Chart">'
    return html_output