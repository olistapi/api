from fastapi import FastAPI, jsonify, HTTPException
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI(title='API e-commerce OLIST',
                description='esta api será utilizada para las consultas que haga la plataforma por streamlit', version="1.0.0")

midb = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'whitny5963',
    database = 'universidad'
)

micursor = midb.cursor()

@app.get("/", response_class=HTMLResponse)
def welcome():
    return """
    <html>
        <head>
            <title>api olist</title>
        </head>
        <body>
            <h1>Bienvenido</h1>
            <h3>A la api de OLIST</h3>
            <img src="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png" style="width:350px">
            <hr>
            <p>Este es nuestro <b>repositorio</b>: <a href="https://github.com/willi-cutzal/Proyecto_Final_OLIST">githhub </a></p>

        </body>
    </html>
    """

@app.get("/alumno")
def get_alumno():
    micursor.execute("SELECT * FROM alumno;")
    result = micursor.fetchall()
    return jsonify(result)