from django.shortcuts import reverse
from django.utils.translation import gettext as _
from django.db import models
from apps.core.models import BaseModel


class OperatorCategory(BaseModel):
    """
        TODO: It is better to use the 'User' class in the future
    """
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service:operator_category__detail', args=(self.id,))

    def get_operators(self):
        return self.operator_set.all()


class Operator(BaseModel):
    name = models.CharField(_('Name'), max_length=100)
    picture = models.ImageField(_('Picture'), upload_to='images/services/operators/pictures/')
    category = models.ForeignKey(OperatorCategory, verbose_name=_('Category'), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service:operator__detail', args=(self.id,))


class OperatorWorkSample(BaseModel):
    operator = models.ForeignKey(Operator, verbose_name=_('Operator'), on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=100)
    image = models.ImageField(_('Image'), upload_to='images/services/operators/work_samples/')
    description = models.TextField(_('Description'), null=True)

    def __str__(self):
        return f'{self.operator} - {self.title[:30]}'
