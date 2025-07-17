import plotly.express as px
import pandas as pd
from data.processor import movies_df

def create_line_budget_revenue():

    decade_revenue = movies_df.groupby('decade')['revenue'].sum().reset_index(name="revenue")
    decade_revenue = decade_revenue.sort_values('decade')
    # print(decade_revenue.head(5))

    decade_budget = movies_df.groupby('decade')['budget'].sum().reset_index(name="budget")
    decade_budget = decade_budget.sort_values('decade')
    # print(decade_budget.head(5))

    decade_budget = decade_budget.drop(columns='decade')

    decade_budget_revenue = pd.concat([decade_revenue, decade_budget], axis = 1, join = "inner")
    decade_budget_revenue = decade_budget_revenue.drop(decade_budget_revenue[(decade_budget_revenue.revenue < 200) | (decade_budget_revenue.budget < 200)].index)

    df_long = decade_budget_revenue.melt(id_vars=['decade'],
                                     value_vars=['revenue', 'budget'],
                                     var_name='metric',
                                     value_name='value')

    fig = px.line(
        df_long,
              x='decade',
              y='value',
              color='metric', # Assigns different colors to 'revenue' and 'budget'
              labels={'value': 'Amount ($)', 'decade': 'Decade', 'metric': 'Metric Type'})

    fig.update_layout(hovermode="x unified")
    # fig.show()

    return fig.to_html(full_html=False)