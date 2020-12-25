from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class Products(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("Name"), max_length=200, unique=True),
        description = models.TextField(_("Description"), blank=True)
    )
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='drjecom_products',null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Ürün")
        verbose_name_plural = _("Ürünler")
    def __str__(self):
        return self.name