"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    dfcredito = pd.read_csv("solicitudes_credito.csv", sep=";")

    dfcredito['sexo'] = dfcredito['sexo'].astype('string')
    dfcredito['tipo_de_emprendimiento'] = dfcredito['tipo_de_emprendimiento'].astype('string')
    dfcredito['idea_negocio'] = dfcredito['idea_negocio'].astype('string')
    dfcredito['barrio'] = dfcredito['barrio'].astype('string')
    dfcredito['comuna_ciudadano'] = dfcredito['comuna_ciudadano'].astype('int')
    dfcredito['monto_del_credito'] = dfcredito['monto_del_credito'].astype('string')
    dfcredito['línea_credito'] = dfcredito['línea_credito'].astype('string')
    dfcredito['fecha1'] = pd.to_datetime(dfcredito['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce')
    dfcredito['fecha2'] = pd.to_datetime(dfcredito['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce')
    dfcredito['fecha_de_beneficio'] = dfcredito['fecha1'].fillna(dfcredito['fecha2'])

    dfcredito = dfcredito.drop(['fecha1'], axis=1)
    dfcredito = dfcredito.drop(['fecha2'], axis=1)

    dfcredito['sexo'] = dfcredito['sexo'].str.lower()
    dfcredito['tipo_de_emprendimiento'] = dfcredito['tipo_de_emprendimiento'].str.lower()
    dfcredito['idea_negocio'] = dfcredito['idea_negocio'].str.lower()
    dfcredito['barrio'] = dfcredito['barrio'].str.lower()
    dfcredito['línea_credito'] = dfcredito['línea_credito'].str.lower()
    

    dfcredito.dropna(inplace=True)
    
    dfcredito["idea_negocio"] = dfcredito["idea_negocio"].str.replace("_", " ")
    dfcredito["idea_negocio"] = dfcredito["idea_negocio"].str.replace("-", " ")
    dfcredito["barrio"] = dfcredito["barrio"].str.replace("_", " ")
    dfcredito["barrio"] = dfcredito["barrio"].str.replace("-", " ")
    dfcredito["línea_credito"] = dfcredito["línea_credito"].str.replace("_", " ")
    dfcredito["línea_credito"] = dfcredito["línea_credito"].str.replace("-", " ")


    dfcredito['monto_del_credito'] = dfcredito['monto_del_credito'].replace('[\$,]', '', regex=True).astype(float)
    

    dfcredito = dfcredito.drop(['Unnamed: 0'], axis=1)
    dfcredito = dfcredito.drop_duplicates()

    return dfcredito