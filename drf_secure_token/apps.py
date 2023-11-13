import django
from django.apps import AppConfig

if django.VERSION < (4, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class DRFSecureTokenConfig(AppConfig):
    name = 'drf_secure_token'
    verbose_name = _('DRF Secure Token')
