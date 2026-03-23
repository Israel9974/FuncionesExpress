
##############################################################################################
#
# PROCEDIMIENTO: Preso Univariado
# @copyright Israel Cornejo 
# FECHA  USUARIO DESCRIPCION:     
#
##############################################################################################

import pandas as pd
import numpy as np
from scipy import stats

def valores_iguales(columna, percentiles):
    """
    Esta función calcula el porcentaje de valores que se repiten entre los percentiles dados.
    """
    columna_limpia = columna.dropna()
    
    if columna_limpia.empty:
        return 9999

    percentil_values = np.percentile(columna_limpia, [p *100  for p in percentiles])
    valor_repetido = stats.mode(columna_limpia).mode

    percentiles_repetidos = []
    for i, valor in enumerate(percentil_values):
        if valor == valor_repetido:
            percentiles_repetidos.append(percentiles[i])

    if percentiles_repetidos:
        inicio = min(percentiles_repetidos)
        fin = max(percentiles_repetidos)
        #print(f"El valor {valor_repetido} se repite desde el percentil {inicio*100} hasta el percentil {fin*100}")
        diferentes = (1- fin) + inicio 
        iguales = 1 - diferentes
        return iguales
    else:
        return 0













