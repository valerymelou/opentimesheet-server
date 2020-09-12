from factory import DjangoModelFactory

from ..models import BaseModel


class BaseFactory(DjangoModelFactory):
    class Meta:
        model = BaseModel
        abstract = True
