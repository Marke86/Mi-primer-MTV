from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def the_simpsons(request):
    familia1=Familia(Nombre="Homero",Apellido="Simpsons", Edad=39 )
    familia2=Familia(Nombre="Marjorie",Apellido="Bouvier", Edad=34 )
    familia3=Familia(Nombre="Bart",Apellido="Simpsons", Edad=10 )
    familia4=Familia(Nombre="Lisa",Apellido="Simpsons", Edad=8 )
    familia5=Familia(Nombre="Maggie",Apellido="Simpsons", Edad=1 )
    familia6=Familia(Nombre="Abraham",Apellido="Simpsons", Edad=86 )

    familia1.save()
    familia2.save()
    familia3.save()
    familia4.save()
    familia5.save()
    familia6.save()

    diccionario={"Nombre1":familia1.Nombre, "Apellido1":familia1.Apellido, "Edad1":familia1.Edad,
                "Nombre2":familia2.Nombre, "Apellido2":familia2.Apellido, "Edad2":familia2.Edad,
                "Nombre3":familia3.Nombre, "Apellido3":familia3.Apellido, "Edad3":familia3.Edad,
                "Nombre4":familia4.Nombre, "Apellido4":familia4.Apellido, "Edad4":familia4.Edad,
                "Nombre5":familia5.Nombre, "Apellido5":familia5.Apellido, "Edad5":familia5.Edad,
                "Nombre6":familia6.Nombre, "Apellido6":familia6.Apellido, "Edad6":familia6.Edad,}
    
    plantilla=loader.get_template("TemFamilia.html")
   
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
