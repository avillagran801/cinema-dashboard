import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64
import io
from data.word_data import word_data

def generate_wordclouds_by_genre():
    """
    Genera un diccionario {genre: HTML img tag} para todos los géneros disponibles.
    """
    wordcloud_dict = {}

    # Obtener géneros únicos
    genres = word_data['genres'].unique()

    for genre in genres:
        # Filtrar sinopsis de ese género
        text = " ".join(word_data[word_data['genres'] == genre]['overview'])

        # Generar wordcloud
        wc = WordCloud(width=800, height=400, background_color='white').generate(text)

        # Convertir en imagen base64
        img_io = io.BytesIO()
        plt.figure(figsize=(8, 4))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(img_io, format='png')
        plt.close()

        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.read()).decode('utf-8')
        img_tag = f"<img src='data:image/png;base64,{img_base64}'/>"

        wordcloud_dict[genre] = img_tag

    return wordcloud_dict
