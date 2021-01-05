from django.db import models
import re 
from django.core.exceptions import ValidationError

def ValidateNumber(value):
    if isinstance(value, int): 
        return value 
    else: 
        raise ValidationError("La identificacion no es un valor numerico") 

def ValidateEmail(email):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return email          
    else:  
        raise ValidationError("El correo no cumple con la estructura") 



class Asistente(models.Model):
    identificacion = models.BigIntegerField(
        unique = True,
        validators =[ValidateNumber],
        error_messages = {
            "unique":"Ya existe la identificacion",
            "required": "Identificacion es necesaria"
        }
    )

    nombres = models.TextField(
        error_messages = {
            "required": "Nombres es necesario"
        }
    )

    apellidos = models.TextField(
        error_messages = {
            "required": "Apellidos es necesario"
        }
    )

    correo_electronico = models.EmailField(
        max_length = 254, 
        unique = True, 
        error_messages = {
            "unique":"Ya existe el correo",
            "required": "correo es necesario"
        },
        validators =[ValidateEmail]
    )

    date_llegada = models.DateTimeField(auto_now_add=True)
