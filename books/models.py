from django.db import models

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(verbose_name='Nombre', max_length=100)
    lastname = models.CharField(verbose_name='Apellidos', max_length=100)
    DICT_NACIONALITY = [
        ('MX', 'México'), ('CO', 'Colombia'), ('EUA', 'Estados Unidos'), ('ES', 'España')
    ]
    nacionality = models.CharField(choices=DICT_NACIONALITY, default='MX', max_length=100)

    def __str__(self):
        return "Escritor: {0} {1} - Nacionalidad: {2}".format(self.firstname, self.lastname, self.nacionality)

    class Meta:
        verbose_name= 'Autor'
        verbose_name_plural= 'Autores'


class Editorial(models.Model):
    name = models.CharField(verbose_name='Editorial', max_length=200)
    phone = models.CharField(verbose_name='Teléfono', max_length=15)
    email = models.CharField(verbose_name='Email', max_length=100)
    facebook = models.URLField(verbose_name='Facebook', max_length=255)
    website = models.URLField(verbose_name='Sitio web', max_length=255)

    def __str__(self):
        return "Editorial: {0} - Teléfono de contacto: {1} - Email: {2} - Web: {3}".format(self.name, self.phone, self.email, self.website)

    class Meta:
        verbose_name= 'Editorial'
        verbose_name_plural= 'Editoriales'


class Books(models.Model):
    editorial_id = models.ForeignKey(Editorial, on_delete=models.CASCADE, verbose_name='Editorial')
    author_id = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='Autor')
    title = models.CharField(verbose_name='Título', max_length=255)
    price = models.DecimalField(verbose_name='Precio', max_digits=9, decimal_places=2)

    def __str__(self):
        return "{0} - {1}".format(self.title, self.price)

    class Meta:
        verbose_name= 'Libro'
        verbose_name_plural= 'Libros'
