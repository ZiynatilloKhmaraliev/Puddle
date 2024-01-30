from django import forms
from .models import Item
INPUT_CLASSSES='w-full py-4 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['category','name','description','price','image']
       
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASSSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSSES
            })


        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name','description','price','image','is_sold']
       
        widgets={
           
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSSES
            })


        }