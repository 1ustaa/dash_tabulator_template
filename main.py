import dash
from dash import dcc, html
from templates import tabulator
import os
import dash_mantine_components as dmc

os.environ['REACT_VERSION'] = '18.2.0'

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    children=dmc.Container([
        dmc.Space(h="xl"),
        dmc.Text(
            fw="700",
            size="xl",
            children="Таблица",
            style={'textAlign': "center"}),
        tabulator()
    ]))

if __name__ == '__main__':
    app.run_server(debug=True)
