from django import forms
from .models import snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.Form):
    name=NameField()
    email=forms.EmailField(label="E-mail")
    category=forms.ChoiceField(choices=[('question','Question'), ('other','Other')])
    subject=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper= FormHelper
        self.helper.form_method = 'post'
        
        self.helper.layout= Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )
    
class SnippetForm(forms.ModelForm):
    
    class Meta:
           model= snippet
           fields= ('name','body')