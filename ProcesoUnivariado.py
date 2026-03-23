
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



## Outliers

def DetectorOutliers(df):
    """
    Devuelve un DataFrame con el número y porcentaje de outliers
    por cada variable numérica del DataFrame original.
    
    La variable queda como índice.
    """
    resultados = []

    for col in df.select_dtypes(include=[np.number]).columns:
        data = df[col].dropna()
        
        # Saltar columnas vacías
        if len(data) == 0:
            resultados.append([col, 0, 0.0])
            continue
        
        # Calcular Q1 y Q3
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1
        
        # Límites
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        # Outliers
        mask_outliers = (data < limite_inferior) | (data > limite_superior)
        num_outliers = mask_outliers.sum()
        porcentaje_outliers = (num_outliers / len(data)) * 100
        
        resultados.append([col, num_outliers, porcentaje_outliers])
    
    # Crear DataFrame con índice = variable
    resumen = pd.DataFrame(resultados, columns=['variable','num_outliers','porcentaje_outliers'])
    resumen.set_index('variable', inplace=True)
    
    return resumen








