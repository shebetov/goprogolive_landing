from django.db import models

# Create your models here.


class SiteEmailLog(models.Model):
    email = models.EmailField(verbose_name="E-Mail")
    ip_addr = models.GenericIPAddressField(verbose_name="IP Address")
    user_agent = models.CharField(max_length=500, verbose_name="User-Agent")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Form E-Mail'
        verbose_name_plural = 'Form E-Mails'
