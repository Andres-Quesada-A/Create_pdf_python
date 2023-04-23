import jinja2  # Importa el módulo jinja2
import pdfkit  # Importa el módulo pdfkit
from datetime import datetime  # Importa la clase datetime del módulo datetime

my_name = "Frank Andres"  # Define la variable my_name
item1 = "TV"  # Define la variable item1
item2 = "Couch"  # Define la variable item2
item3 = "Washing Machine"  # Define la variable item3
today_date = datetime.today().strftime("%d %b, %Y")  # Define la variable today_date con la fecha actual en formato de cadena

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}  # Crea un diccionario con los datos que se usarán en la plantilla

template_loader = jinja2.FileSystemLoader('./')  # Crea un objeto FileSystemLoader para cargar la plantilla HTML
template_env = jinja2.Environment(loader=template_loader)  # Crea un objeto Environment para cargar la plantilla HTML

html_template = 'basic-template.html'  # Define el nombre del archivo de la plantilla HTML
template = template_env.get_template(html_template)  # Carga la plantilla HTML en un objeto Template
output_text = template.render(context)  # Renderiza la plantilla con los datos del diccionario y guarda el resultado en una variable

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  # Crea un objeto de configuración para pdfkit
output_pdf = 'pdf_generated.pdf'  # Define el nombre del archivo PDF generado
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')  # Genera un archivo PDF usando pdfkit y los datos renderizados en la plantilla HTML
