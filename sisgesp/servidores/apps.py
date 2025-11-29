from django.apps import AppConfig

class ServidoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sisgesp.servidores'  # ← Caminho completo
    verbose_name = 'Gestão de Servidores'