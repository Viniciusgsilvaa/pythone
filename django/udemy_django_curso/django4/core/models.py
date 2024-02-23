from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    
    class Meta:
        abstract = True


class Portifolio(Base):
    cabecalio = models.CharField('Cabeçalio', max_length=50)
    sublinha = models.CharField('Sublinha', max_length=15)
    sobre = models.CharField('Sobre', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 600, 'height': 450, 'crop': True}})

    def __str__(self):
        return self.cabecalio
