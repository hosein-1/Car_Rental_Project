from django.db import models
from django.conf import settings


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode='utf-8')
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه'

    def __str__(self):
        return f'{self.title}'


class Questions(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'سوالات'
        verbose_name_plural = 'سوالات'

    @property
    def children(self):
        return Questions.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
