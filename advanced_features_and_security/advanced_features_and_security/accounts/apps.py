
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advanced_features_and_security.accounts'  # full dotted path
    label = 'accounts'  # app label stays 'accounts'
