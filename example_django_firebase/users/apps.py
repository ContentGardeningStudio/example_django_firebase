from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "example_django_firebase.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import example_django_firebase.users.signals  # noqa F401
        except ImportError:
            pass
