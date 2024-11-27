from django.db import models

class Credentials(models.Model):
    name_account = models.CharField(max_length=70, verbose_name='Nombre del correo')
    email_account = models.EmailField(verbose_name='Correo de envio')
    password_account = models.CharField(max_length=16, verbose_name='Contraseña de aplicacion')
    is_active = models.BooleanField(default=False, verbose_name='¿Cuenta activa?')

    def save(self, *args, **kwargs):
        if self.is_active:
            # Si este registro se marca como activo, desactivar los demás
            Credentials.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Credenciales'  
        verbose_name_plural = 'Credenciales' 

