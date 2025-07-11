import plotly.express as px
import numpy as np 
import pandas as pd 
import matplotlib as mpl #
import matplotlib.pyplot as plt #
# from data.processor import get_movies_by_genre
from processor import get_top100_revenue_movies

print(get_top100_revenue_movies().head(5))