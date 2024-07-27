from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    """
    This class configures the 'newsletter' application.

    Attributes:
        default_auto_field (str): Specifies the type of field to use for
        auto-generated primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resources'
