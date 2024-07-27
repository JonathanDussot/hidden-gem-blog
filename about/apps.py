from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    This class configures the 'about' application.

    Attributes:
        default_auto_field (str): Specifies the type of field to use for
        auto-generated primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
