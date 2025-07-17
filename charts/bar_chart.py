import plotly.express as px
import plotly.io as pio
from data.bar_data import people_in_movies

def create_top10_actors_bar():
    df = people_in_movies.copy().reset_index()
    df['cast'] = df['cast'].fillna('')
    df_exploded = df.assign(actor=df['cast'].str.split(',')).explode('actor')
    df_exploded['actor'] = df_exploded['actor'].str.strip()
    df_exploded = df_exploded[df_exploded['actor'] != '']

    actor_counts = df_exploded.groupby('actor')['id'].nunique().reset_index()
    actor_counts.columns = ['actor', 'num_movies']
    top10_actors = actor_counts.sort_values(by='num_movies', ascending=False).head(10)

    fig = px.bar(
        top10_actors,
        x='actor',
        y='num_movies',
        title='Top 10 Actors',
        labels={'actor': 'Actors', 'num_movies': 'Number of movies'}
    )
    fig.update_layout(
        height=500,
        width=700,
        margin={"r": 20, "t": 50, "l": 20, "b": 100},
        xaxis_tickangle=-45,
        xaxis=dict(domain=[0.05, 0.95], automargin=False, title_standoff=10)
    )
    return pio.to_html(fig, full_html=False)


def create_top10_writers_bar():
    df = people_in_movies.copy().reset_index()
    df['writers'] = df['writers'].fillna('')
    df_exploded = df.assign(writer=df['writers'].str.split(',')).explode('writer')
    df_exploded['writer'] = df_exploded['writer'].str.strip()
    df_exploded = df_exploded[df_exploded['writer'] != '']

    writer_counts = df_exploded.groupby('writer')['id'].nunique().reset_index()
    writer_counts.columns = ['writer', 'num_movies']
    top10 = writer_counts.sort_values(by='num_movies', ascending=False).head(10)

    fig = px.bar(
        top10,
        x='writer',
        y='num_movies',
        title='Top 10 Writers',
        labels={'writer': 'Writers', 'num_movies': 'Number of movies'}
    )
    fig.update_layout(
        height=500,
        width=700,
        margin={"r": 20, "t": 50, "l": 20, "b": 100},
        xaxis_tickangle=-45,
        xaxis=dict(domain=[0.05, 0.95], automargin=False, title_standoff=10)
    )
    return pio.to_html(fig, full_html=False)


def create_top10_directors_bar():
    df = people_in_movies.copy().reset_index()
    df['director'] = df['director'].fillna('')
    df = df[df['director'].str.strip() != '']

    director_counts = df.groupby('director')['id'].nunique().reset_index()
    director_counts.columns = ['director', 'num_movies']
    top10 = director_counts.sort_values(by='num_movies', ascending=False).head(10)

    fig = px.bar(
        top10,
        x='director',
        y='num_movies',
        title='Top 10 Directors',
        labels={'director': 'Directors', 'num_movies': 'Number of movies'}
    )
    fig.update_layout(
        height=500,
        width=700,
        margin={"r": 20, "t": 50, "l": 20, "b": 100},
        xaxis_tickangle=-45,
        xaxis=dict(domain=[0.05, 0.95], automargin=False, title_standoff=10)
    )
    return pio.to_html(fig, full_html=False)
