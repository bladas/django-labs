from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    slug = forms.SlugField()

    class Meta:
        model = Category
        fields = '__all__'
