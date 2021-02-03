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

nomes = pd.read_csv('input/sp_hard2.csv', encoding = 'utf-8')

wage_gaps = wage_gaps.merge(nomes, left_on = 'Mun', right_on = 'code' )

# Create figure
fig = go.Figure()


fig.add_trace(go.Choropleth(geojson = mapa_mun_sp,
                            featureidkey = "properties.CD_GEOCMU",
                            locations = wage_gaps['Mun'],
                            z = wage_gaps['gap_negros'],
                            text = wage_gaps['name'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença salarial <br> (negros - brancos)",
                            marker_line_color = 'white',
                            marker_line_width = 0.8))

fig.update_layout(
    title_text = 'Gap Salarial entre Negros e Brancos',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre negros e brancos controlando por idade,"
                             "ocupação, setor e sexo. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             'Valores < 0 indicam salários menores para negros quando comparados a brancos.'
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
                            text = wage_gaps['name'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença salarial <br> (mulheres - homens)",
                            marker_line_color = 'white',
                            marker_line_width = 0.8))

fig.update_layout(
    title_text = 'Gap Salarial entre Mulheres e Homens',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre mulheres e homens controlando por idade,"
                             "ocupação, setor e raça. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             'Valores < 0 indicam salários menores para mulheres quando comparadas aos homens.'
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
