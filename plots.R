library(plotly)
library(rjson)
library(htmlwidgets)

setwd('C:/Users/Lucas/Desktop/rais-wage-gap/')

mapa <- fromJSON(file = 'input/sp_simple.geojson')

wage_gaps = read.csv('tmp/wage_gaps.csv', header = T)


# o codigo IBGE do geojson tem 7 digitos :/

for (n in 1:645) {

  
  mapa[["features"]][[n]][["properties"]][["CD_GEOCMU"]] = floor(mapa[["features"]][[n]][["properties"]][["CD_GEOCMU"]]/10)
  
    
}


# Escolha um n�vel de signific�ncia

p_valor <- 0.10

wage_gaps <- wage_gaps %>% 
              mutate(gap_negros = replace(gap_negros, p_valor_negros > p_valor, 0),
                     gap_mulheres = replace(gap_mulheres, p_valor_mulheres > p_valor, 0))



#--------------------------------------------------------------------------------
#------------------------------------- Plots ------------------------------------
#--------------------------------------------------------------------------------

g <- list(
  fitbounds = "locations",
  visible = FALSE
)

fig <- plot_ly() 
fig <- fig %>% add_trace(
               type = "choropleth",
               geojson = mapa,
               locations = wage_gaps$Mun,
               z = wage_gaps$gap_negros,
               colorscale = "RdGy",
               featureidkey = "properties.CD_GEOCMU"
)

fig <- fig %>% layout(
  geo = g
)

fig <- fig %>% colorbar(title = "Diferen�a \n (log sal�rio/hora)")
fig <- fig %>% layout(
  title = "Diferen�a Salarial entre Negros e Brancos nos Munic�pios Paulistas",
  annotations = 
    list(x = 0.5,
         y = -0.005,
         text = paste("Diferen�a no log(sal�rio/h) entre negros e brancos controlando por idade,",
         "ocupa��o, setor e sexo. <br> C�lculos a partir dos microdados da RAIS 2019.",
         "Coeficientes n�o significativos a 10% foram considerados zero."), 
         showarrow = F,
         xref='paper',
         yref='paper', 
         xanchor='center',
         yanchor='auto',
         xshift=0,
         yshift=0
        )
  
)

f <- "tmp/gap_negros.html"
saveWidget(fig,file.path(normalizePath(dirname(f)),basename(f)), selfcontained = F)



#---------------------------------------------------------------------------------



g <- list(
  fitbounds = "locations",
  visible = FALSE
)

fig <- plot_ly() 
fig <- fig %>% add_trace(
  type = "choropleth",
  geojson = mapa,
  locations = wage_gaps$Mun,
  z = wage_gaps$gap_mulheres,
  colorscale = "RdGy",
  featureidkey = "properties.CD_GEOCMU"
)

fig <- fig %>% layout(
  geo = g
)

fig <- fig %>% colorbar(title = "Diferen�a \n (log sal�rio/hora)")
fig <- fig %>% layout(
  title = "Diferen�a Salarial entre Mulheres e Homens nos Munic�pios Paulistas",
  annotations = 
    list(x = 0.5,
         y = -0.005,
         text = paste("Diferen�a no log(sal�rio/h) entre mulheres e homens controlando por idade,",
                      "ocupa��o, setor e ra�a. <br> C�lculos a partir dos microdados da RAIS 2019.",
                      "Coeficientes n�o significativos a 10% foram considerados zero."), 
         showarrow = F,
         xref='paper',
         yref='paper', 
         xanchor='center',
         yanchor='auto',
         xshift=0,
         yshift=0
    )
  
)

f <- "tmp/gap_mulheres.html"
saveWidget(fig,file.path(normalizePath(dirname(f)),basename(f)), selfcontained = F)
