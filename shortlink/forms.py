from django.forms import ModelForm, TextInput, NumberInput
from .models import RedirectLink


class RdirLink(ModelForm):
    class Meta:
        model = RedirectLink
        fields = ('url', 'stop_count', 'stop_date')
        widgets = {
            'url': TextInput(attrs={'placeholder':'Ссылка, которую необходмо сократить'}),
            'stop_count': NumberInput(attrs={'placeholder':'Кол-во переходов'}),
            'stop_date': TextInput(attrs={'placeholder':'Дата отключения'}),
        }