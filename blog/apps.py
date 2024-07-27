from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    This class configures the 'blog' application.

    Attributes:
        default_auto_field (str): Specifies the type of field to use for
        auto-generated primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
