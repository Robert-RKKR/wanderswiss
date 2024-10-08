# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseStringChoices


# Choices class:
class LanguageChoices(BaseStringChoices):

    # Choices values:
    DE = 'de', _('German')
    EN = 'en', _('English')
    GE = 'pl', _('Polish')
