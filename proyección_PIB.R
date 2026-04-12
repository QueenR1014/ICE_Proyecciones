library(readxl)
library(dplyr)
# Inserción PIB por oferta

PIB_oferta = read_excel("Cuadros_Prod_Gasto.xlsx", sheet = "PIB oferta anual NORMAL")
PIB_oferta = select(PIB_oferta, 2:22)
PIB_oferta = na.omit(PIB_oferta)
# Convertir primera fila en nombres de columnas
colnames(PIB_oferta) = PIB_oferta[1, ]
PIB_oferta = PIB_oferta[-1, ]


datos = as.data.frame(t(PIB_oferta[1:15, 1:21]))
colnames(datos) = PIB_oferta[[1]][1:15]


model = lm(PIB ~ ., data = datos)
summary(model)


