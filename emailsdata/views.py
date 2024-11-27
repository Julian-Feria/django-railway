import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmailsData

def emails_list(request):
    # Procesamiento del archivo Excel si se envía un archivo
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        try:
            # Lee el archivo Excel directamente desde el archivo en memoria
            df = pd.read_excel(excel_file)
            # print(df)
            # print("Columnas en el archivo:", df.columns)

            # Verifica que el archivo contenga la columna 'email'
            if 'email' not in df.columns:
                messages.error(request, "El archivo debe contener una columna 'email'.")
                return redirect("emails_list")

            # Itera sobre cada fila del DataFrame y guarda en el modelo
            for index, row in df.iterrows():
                email = row['email']
                
                # Crea un registro solo si el email no existe para evitar duplicados
                EmailsData.objects.get_or_create(email=email)
            
            messages.success(request, "Los datos han sido cargados exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {e}")
        
        return redirect("emails_list")

    # Obtiene todos los registros de EmailsData para mostrarlos en la tabla
    emails = EmailsData.objects.all()
    return render(request, "emailsdata/emails_list.html", {"emails": emails})
