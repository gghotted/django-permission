# coding=utf-8
import django

try:
    import collections
    def isiterable(x):
        return isinstance(x, collections.Iterable)
except ImportError:
    def isiterable(x):
        try:
            iter(x)
            return True
        except TypeError:
            return False

try:
    from django.template.base import add_to_builtins
except ImportError:
    from django.template.loader import add_to_builtins

try:
    # django.utils.importlib is removed from Django 1.9
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module

try:
    # Django 1.7 or over use the new application loading system
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model

try:
    # Python 3
    from urllib.parse import urlparse
except ImportError:
    # Python 2
    from urlparse import urlparse
