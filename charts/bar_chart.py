import plotly.express as px
import plotly.io as pio
from data.bar_data import people_in_movies

def create_top10_actors_bar():
    return
    df = people_in_movies.copy()
    df['cast'] = df['cast'].fillna('')

    # Separar en actores individuales
    df_exploded = df.assign(actor=df['cast'].str.split(',')).explode('actor')
    df_exploded['actor'] = df_exploded['actor'].str.strip()

    # Contar cuántas películas tiene cada actor
    actor_counts = df_exploded.groupby('actor')['id'].nunique().reset_index()
    actor_counts.columns = ['actor', 'num_movies']

    # Top 10 actores por ahora, luego veré lo de directores y escritores
    top10_actors = actor_counts.sort_values(by='num_movies', ascending=False).head(10)

    fig = px.bar(
        top10_actors,
        x='actor',
        y='num_movies',
        title='Top 10 Actores con más películas',
        labels={'actor': 'Actor', 'num_movies': 'Número de Películas'},
        color='num_movies',
        color_continuous_scale='Viridis'
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        height=500,
        margin={"r": 20, "t": 50, "l": 20, "b": 100},
    )

    return pio.to_html(fig, full_html=False)
