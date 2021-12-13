import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



class Data_frame:   

    def __init__(self,data_frame=None):
        self.data_frame =data_frame
        self.programas=None
        self.diccionario={}
             
    def Generar_tabla2(self,diccio):
        keys= list(diccio.keys())
        valores= list(diccio.values())
        print(diccio)        
        if 'Todos' in valores and 'entidad_territorial' in keys:
            aux = self.data_frame.groupby(['entidad_territorial'],as_index=False).agg({
            'n_mero_acumulado_de_1_dosis':'sum',
            'n_mero_acumulado_de_esquema':'sum'
            })
            return aux
        elif valores[0]!='Todos' and 'entidad_territorial' in keys:
            df = self.data_frame.groupby(['entidad_territorial','municipio'],as_index=False).agg({
            'n_mero_acumulado_de_1_dosis':'sum',
            'n_mero_acumulado_de_esquema':'sum'
            })
            df=df[df['entidad_territorial']==valores[0]]
            return df
        elif 'Todos' in valores and 'year' in keys:
            aux = self.data_frame.groupby(['grupo_edad'],as_index=False).agg({
                'n_mero_acumulado_de_1_dosis':'sum',
                'n_mero_acumulado_de_esquema':'sum'
            })
            return aux    
        elif valores[0]!='Todos' and 'year' in keys:
            aux = self.data_frame.groupby(['entidad_territorial','grupo_edad'],as_index=False).agg({
                'n_mero_acumulado_de_1_dosis':'sum',
                'n_mero_acumulado_de_esquema':'sum'
            })
            aux=aux[aux['grupo_edad']==valores[0]]
            return aux    
                

    def Set_dataframe(self,df):
        self.data_frame=df
        self.data_frame['n_mero_acumulado_de_1_dosis']=self.data_frame['n_mero_acumulado_de_1_dosis'].astype(int)
        self.data_frame['n_mero_acumulado_de_esquema']=self.data_frame['n_mero_acumulado_de_esquema'].astype(int)
        self.data_frame=self.data_frame.drop(self.data_frame[(self.data_frame['grupo_edad']=='No definido')|(self.data_frame['grupo_edad']=='Todas')].index)
        aux = self.data_frame.groupby(['entidad_territorial'],as_index=False).agg({
            'n_mero_acumulado_de_1_dosis':'sum',
            'n_mero_acumulado_de_esquema':'sum'
        })
        self.programas=aux['entidad_territorial']
    
    def Grupo_edad(self):
        aux = self.data_frame.groupby(['grupo_edad'],as_index=False).agg({
            'n_mero_acumulado_de_1_dosis':'sum',
            'n_mero_acumulado_de_esquema':'sum'
        })
        valor=aux['grupo_edad']
        return valor
        

    def Get_programs(self):
        return self.programas