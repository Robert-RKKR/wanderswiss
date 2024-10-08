# Django - translation import:
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

# WanderSwiss - model import:
from infopedia.models.article_model import ArticleModel


# Translation class:
class ArticleTranslation(TranslationOptions):
    fields = ('name', 'content', 'description',)


# Register translation:
translator.register(ArticleModel, ArticleTranslation)
