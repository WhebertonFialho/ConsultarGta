from flask import Flask, jsonify, request
import os
from API import ConsultarGTA as GTA

app = Flask(__name__)
app.secret_key = 'development key'
app.debug = True

@app.route('/')
def index():
    return jsonify(status="It's Work")

@app.route('/consultarGtaPorCodBarra', methods = ['GET'] )
def consultarGtaPorCodBarra():
    cod_barra = request.args.get('codBarra', default='', type=str)
   
    resultado = GTA.consultarGtaPorCodBarra(cod_barra)
    return jsonify(resultado)

@app.route('/consultarGtaPorNroGta', methods = ['GET'])
def consultarGtaPorNroGta():
    nro_gta = request.args.get('nroGta', default='', type=str)
    serie = request.args.get('serie', default='', type=str)
    estado = request.args.get('estado', default='', type=str)
    
    resultado = GTA.consultarGtaPorNroGta(nro_gta, serie.upper(), estado.upper())
    return jsonify(resultado)

if __name__ == '__main__':
    app.run()
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)