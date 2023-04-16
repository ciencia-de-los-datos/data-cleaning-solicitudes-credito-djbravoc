"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df['sexo'] = df['sexo'].astype('string')
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype('string')
    df['idea_negocio'] = df['idea_negocio'].astype('string')
    df['barrio'] = df['barrio'].astype('string')
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int')
    df['monto_del_credito'] = df['monto_del_credito'].astype('string')
    df['línea_credito'] = df['línea_credito'].astype('string')
    df['fecha1'] = pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce')
    df['fecha2'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce')
    df['fecha_de_beneficio'] = df['fecha1'].fillna(df['fecha2'])

    df= df.drop(['fecha1'], axis=1)
    df= df.drop(['fecha2'], axis=1)

    df['sexo']=df['sexo'].str.lower()
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio']=df['idea_negocio'].str.lower()
    df['barrio']=df['barrio'].str.lower()
    df['línea_credito']=df['línea_credito'].str.lower()
    df

    df.dropna(inplace=True)
    

    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")



    df['monto_del_credito'] = df['monto_del_credito'].replace('[\$,]', '', regex=True).astype(float)
    

    df= df.drop(['Unnamed: 0'], axis=1)
    df = df.drop_duplicates()

    #
    # Inserte su código aquí
    #

    return df