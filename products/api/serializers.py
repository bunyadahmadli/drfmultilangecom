from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from products.models import Products
from .mixins import TranslatedSerializerMixin


class ProductSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Products)
    class Meta:
        model = Products
        fields = ('translations' ,'author', 'created_on', 'updated_on')