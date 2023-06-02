
from django.conf import settings
from django.core.validators import FileExtensionValidator
import os

image_validator = FileExtensionValidator(
    allowed_extensions = ['png', 'jpeg', 'jpg'], 
    message = "Sólo se permite formato PNG, JPEG, JPG.",
    code = 'formato_invalido'
)

