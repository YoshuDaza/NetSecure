from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

def sql_injection(request):
    return render(request, 'sql_injection.html')

def sql_injection(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        # Realizamos la prueba de SQL Injection y generamos un reporte
        reporte = generar_reporte_sql_injection(url)

        # Renderizamos la página con el reporte del escaneo
        return render(request, 'sql_injection.html', {'reporte': reporte})

    return render(request, 'sql_injection.html')

def generar_reporte_sql_injection(url):
    reporte = {}
    detalles = []
    
    try:
        # Simulación de prueba con payload de SQL Injection
        payload = "' OR 1=1 --"
        response = requests.get(f"{url}?input={payload}")

        # Si encontramos algún mensaje de error que podría indicar una vulnerabilidad
        if "error" in response.text or "syntax" in response.text:
            reporte['vulnerabilidad'] = "¡Vulnerabilidad detectada! La URL es susceptible a SQL Injection."
            detalles.append(f"Payload utilizado: {payload}")
            detalles.append(f"Respuesta del servidor: {response.text[:500]}... (limitado a 500 caracteres)")
            
            # Generamos recomendaciones para mitigar el SQLi
            recomendaciones = [
                "Usar consultas preparadas (Prepared Statements) para evitar la inyección SQL.",
                "Validar y sanitizar todos los datos de entrada del usuario.",
                "Restringir los permisos de la base de datos para que solo las operaciones necesarias sean permitidas.",
                "Configurar políticas de seguridad y monitorear el tráfico de red para detectar actividad sospechosa.",
                "Realizar pruebas periódicas de seguridad con herramientas automáticas y manuales."
            ]
            reporte['recomendaciones'] = recomendaciones
        else:
            reporte['vulnerabilidad'] = "No se detectaron vulnerabilidades de SQL Injection en la URL proporcionada."
            detalles.append(f"Payload utilizado: {payload}")
            detalles.append("No se encontraron patrones de error en la respuesta del servidor.")
            reporte['recomendaciones'] = [
                "Mantener buenas prácticas de desarrollo seguro.",
                "Continuar con el monitoreo regular de vulnerabilidades.",
                "Actualizar las políticas de seguridad según sea necesario."
            ]
        
        reporte['detalles'] = "\n".join(detalles)

    except Exception as e:
        reporte['vulnerabilidad'] = "Error al realizar el escaneo."
        reporte['detalles'] = f"Error: {str(e)}"
        reporte['recomendaciones'] = ["Revisa la URL proporcionada o los permisos del servidor."]
    
    return reporte

@login_required
def sql_injection(request):
    return render(request, 'sql_injection.html')