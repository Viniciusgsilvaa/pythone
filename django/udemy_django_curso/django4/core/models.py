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
    
    class Meta:
        verbose_name='Portifolio'
        verbose_name_plural='Portifolios'


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=50)

    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=30)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 500, 'height': 500, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    x = models.CharField('x', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name='Funcionario'
        verbose_name_plural='Funcionarios'
    
    def __str__(self):
        return self.nome

class Sobre(Base):
    data = models.CharField('Data', max_length=50)
    cabecalio = models.CharField('Cabeçalio', max_length=50)
    sobre = models.CharField('Sobre', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 200, 'height': 200, 'crop':True}})

    class Meta:
        verbose_name='Sobre'
    
    def __str__(self):
        return self.data