from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import subprocess

# Create your views here.

def sql_injection(request):
    return render(request, 'sql_injection.html')

def sql_injection(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        reporte = ejecutar_sqlmap(url)

        return render(request, 'sql_injection.html', {'reporte': reporte})

    return render(request, 'sql_injection.html')


def ejecutar_sqlmap(url):
    sqlmap_path = "/sqlmap-dev/sqlmap.py"  

    command = ["python3", sqlmap_path, "-u", url, "--batch", "--risk=1", "--level=2", "--output-dir=/tmp/sqlmap_output"]

    try:
        # Ejecutar el comando
        process = subprocess.run(command, capture_output=True, text=True, timeout=300)
        output = process.stdout  # Captura el resultado del escaneo

        # Parsear el resultado del escaneo
        if "is vulnerable" in output:
            vulnerabilidad = "¡La URL es vulnerable a SQL Injection!"
        else:
            vulnerabilidad = "La URL no parece ser vulnerable a SQL Injection."

        # Retornar un reporte con el resultado y el output del escaneo
        reporte = {
            'vulnerabilidad': vulnerabilidad,
            'detalles': output,
            'recomendaciones': [
                "Usar consultas preparadas (Prepared Statements).",
                "Validar y sanitizar entradas del usuario.",
                "Implementar políticas de control de acceso adecuadas.",
                "Realizar pruebas de seguridad regularmente."
            ]
        }

    except subprocess.TimeoutExpired:
        reporte = {
            'vulnerabilidad': "El escaneo ha excedido el tiempo límite.",
            'detalles': "Intenta nuevamente más tarde o con otra URL.",
            'recomendaciones': []
        }

    except Exception as e:
        reporte = {
            'vulnerabilidad': "Error durante el escaneo.",
            'detalles': str(e),
            'recomendaciones': []
        }

    return reporte

@login_required
def sql_injection(request):
    return render(request, 'sql_injection.html')