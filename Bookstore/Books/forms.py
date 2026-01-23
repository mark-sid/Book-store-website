from django import forms
from .models import Category


class CategorySelectForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        to_field_name='slug',
        empty_label='All Categories',
        widget=forms.Select(attrs={'onchange': 'this.form.submit()'}),
<<<<<<< HEAD
=======
        required=False
>>>>>>> 54c77019738af15dfe5148add3b6254c0c648837
    )

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', Category.objects.all())
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = queryset

