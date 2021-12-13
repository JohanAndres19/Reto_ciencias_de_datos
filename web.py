from flask  import Flask, render_template,request
import pandas as pd
import json
import io
import base64
from data_frame import *
from sodapy import Socrata
app = Flask(__name__)

Dframe=Data_frame()

@app.before_first_request
def before_request():
    cliente = Socrata("www.datos.gov.co", None)
    resultado = cliente.get("8cgj-t5ds",limit=10100)
    Dframe.Set_dataframe(pd.DataFrame.from_records(resultado))
    print(Dframe.Get_programs())
    


@app.route('/',methods=['GET','POST'])
def Index():
    if request.method=='GET':
        programas=Dframe.Get_programs()
        return render_template('index.html',programas=programas,edad=Dframe.Grupo_edad())  


@app.route('/peticion', methods=["POST"])
def nueva_ruta():
    response ={}
    datos={}
    valores=list(request.form.values())
    keys=list(request.form.keys()) 
    for i in range(len(valores)):
        if valores[i]!='':
            datos[keys[i]]=valores[i]

    df=Dframe.Generar_tabla2(datos)
    response['tabla']=df.to_html(classes='data', header=True, index=False)
    return json.dumps(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True )