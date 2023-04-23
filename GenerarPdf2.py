import jinja2  # Importa el módulo jinja2
import pdfkit  # Importa el módulo pdfkit
from datetime import datetime  # Importa la clase datetime del módulo datetime



Encabezado = "<!DOCTYPE html><html lang='en'><head>    <meta charset='UTF-8'>    <meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body>    <hr />    <h1 style='text-align: center;'><strong>"
Encabezado2 = "</strong></h1> </br> <h2  style='text-align: center;'>"
Encabezado3 = "</h2><hr />   "

salto = '</br>'

Apertura = "<p>"
Cierre = "</p>"

NombreEvento= "Evento"
Prueba = "Prueba"
aperturaTabla = "<table>"
cierreTabla = "</table>"

encabezadoTabla = "<thead><tr><th>Nombre Atleta</th><th>Dorsal</th><th>Marca</th><th>Lugar</th></tr></thead>"

AperturaBody = "<tbody>"
CierreBody = "</tbody>"

AperturaLinea = "<tr>"
CierreLinea = "</tr>"

AperturaCelda = "<td>"
CierreCelda = "</td>"






def GenerarPDF (title, subTitle, Contenido):
    today_date = datetime.today().strftime("%d %b, %Y")  # Define la variable today_date con la fecha actual en formato de cadena

    output_text = Encabezado + title + Encabezado2 + subTitle + Encabezado3

    for evento in Contenido:
        output_text += Apertura + NombreEvento + " " + evento['idEvento'] + ": " + evento['nombreEvento'] + Cierre
        output_text += Apertura + Prueba + " " + evento['idPrueba'] + ": " + evento['nombrePrueba'] + Cierre
        output_text += aperturaTabla + encabezadoTabla + AperturaBody
        
        for atleta in evento['atletas']:
            output_text += AperturaLinea
            output_text += AperturaCelda + atleta['nombreAtleta'] + CierreCelda
            output_text += AperturaCelda + atleta['dorsal'] + CierreCelda
            output_text += AperturaCelda + atleta['marca'] + CierreCelda
            output_text += AperturaCelda + atleta['Lugar'] + CierreCelda
            output_text += CierreLinea

        output_text += CierreBody + cierreTabla


    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  # Crea un objeto de configuración para pdfkit
    output_pdf = 'pdf_generated.pdf'  # Define el nombre del archivo PDF generado
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')  # Genera un archivo PDF usando pdfkit y los datos renderizados en la plantilla HTML
 

# def GenerarPDF (Titulo, item1, item2, item3, Informacion_extra, Mas_info):

title = "APLICACIÓN EVENTOS DE ATLETISMO"
subTitle = "MARCAS POR EVENTO"

Contenido = [
    {
        'idEvento': "1",
        'nombreEvento': "Nombre del evento",
        'idPrueba': '2',
        'nombrePrueba': 'Nombre de la prueba',
        'atletas': [
            {
                'nombreAtleta': 'Nombre 1',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar': "1"
            },
            {
                'nombreAtleta': 'Nombre 2',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"2"
            },
            {
                'nombreAtleta': 'Nombre 3',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"3"
            },
        ]
    },
    {
        'idEvento': "432",
        'nombreEvento': "Nombre del evento 5345",
        'idPrueba': '534534',
        'nombrePrueba': 'Nombre de la prueba 53453',
        'atletas': [
            {
                'nombreAtleta': 'Nombre 1',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar': "1"
            },
            {
                'nombreAtleta': 'Nombre 2',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"2"
            },
            {
                'nombreAtleta': 'Nombre 3',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"3"
            },
             {
                'nombreAtleta': 'Nombre 2',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"2"
            },
            {
                'nombreAtleta': 'Nombre 3',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"3"
            },
        ]
    },
    {
        'idEvento': "342421",
        'nombreEvento': "Nomfgdssgfd",
        'idPrueba': '2654645',
        'nombrePrueba': 'Nofdgdsf',
        'atletas': [
            {
                'nombreAtleta': 'Nombre 1',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar': "1"
            },
            {
                'nombreAtleta': 'Nombre 2',
                'dorsal': 'algo para el dorsal',
                'marca': 'marca ',
                'Lugar':"2"
            },
        ]
    }
]
GenerarPDF(title, subTitle, Contenido)