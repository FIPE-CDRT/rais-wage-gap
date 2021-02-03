# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:03:14 2021

@author: Lucas
"""

import os
import plotly.graph_objects as go
import pandas as pd
import json

os.chdir('C:/Users/Lucas/Desktop/rais-wage-gap')

wage_gaps = pd.read_csv('tmp/wage_gaps.csv')


with open('input/sp_simple3.geojson', encoding='utf-8') as response:    
    mapa_mun_sp = json.load(response)





# Create figure
fig = go.Figure()


fig.add_trace(go.Choropleth(geojson = mapa_mun_sp,
                            featureidkey = "properties.CD_GEOCMU",
                            locations = wage_gaps['Mun'],
                            z = wage_gaps['gap_negros'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença \n (log salário/hora)",
                            marker_line_color = 'darkgray',
                            marker_line_width = 0.5))

fig.update_layout(
    title_text = 'Gap Salarial entre Negros e Brancos',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre negros e brancos controlando por idade,"
                             "ocupação, setor e sexo. <br> Cálculos a partir dos microdados da RAIS 2019."
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )]    
)

fig.update_geos(fitbounds = 'locations',
                visible = False)

fig.write_html("tmp/gap_racial.html",
               include_plotlyjs="cdn")


#------------------------------------------------------------------------------


# Create figure
fig = go.Figure()


fig.add_trace(go.Choropleth(geojson = mapa_mun_sp,
                            featureidkey = "properties.CD_GEOCMU",
                            locations = wage_gaps['Mun'],
                            z = wage_gaps['gap_mulheres'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença \n (log salário/hora)",
                            marker_line_color = 'darkgray',
                            marker_line_width = 0.5))

fig.update_layout(
    title_text = 'Gap Salarial entre Mulheres e Homens',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre mulheres e homens controlando por idade,"
                             "ocupação, setor e raça. <br> Cálculos a partir dos microdados da RAIS 2019."
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )]    
)

fig.update_geos(fitbounds = 'locations',
                visible = False)

fig.write_html("tmp/gap_genero.html",
               include_plotlyjs="cdn")




