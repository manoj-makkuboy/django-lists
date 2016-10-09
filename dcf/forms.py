# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from dcf.models import Item, Group, Image, CustomUser

# django-registration app integration
from registration.forms import RegistrationForm




class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ('phone','receive_news','first_name','last_name','username','is_active','user_email')


class SearchForm(forms.Form):
    group = forms.ModelChoiceField(label=_('Group'), queryset=Group.objects.all(), required=False)
    q = forms.CharField(required=False, label=_('Query'),)

    def filter_by(self):
        # TODO search using more than one field
        # TODO split query string and make seaprate search by words
        filters = {}
        if self.cleaned_data['group'] is not None:
            filters['group'] = self.cleaned_data['group']
        filters['description__icontains'] = self.cleaned_data['q']

        return filters


class ItemCreateEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('group', 'title', 'description', 'price', 'phone', 'is_active')


class AdImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('owner',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('phone', )
