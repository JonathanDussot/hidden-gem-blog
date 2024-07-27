from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    This class configures the 'about' application.

    Attributes:
        default_auto_field (str): Specifies the type of field to use for
        auto-generated primary keys. 'BigAutoField' is used to accommodate
        larger integers. name (str): The name of the application. This is
        used by Django to refer to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
