# This file ensures Django loads the models from your custom folder
from .model.model import Todo  # relative import to model file
__all__ = ['Todo']


# Create your models here.
