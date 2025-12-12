from django import forms

class CategorySelectForm(forms.Form):
    category_slug = forms.ChoiceField(
        choices=[('', 'All Categories')],
        widget=forms.Select(attrs={'onchange': 'this.form.submit()'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories', [])
        super().__init__(*args, **kwargs)
        self.fields['category_slug'].choices += [(category.slug, category.name) for category in categories]

    def clean_category_slug(self):
        category_slug = self.cleaned_data.get('category_slug')
        if category_slug == '':
            return None
        return category_slug
