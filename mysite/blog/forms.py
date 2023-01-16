from django import forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):
    #set up fields for form 
    class Meta():
        model = Post 
        fields = ('author', 'title', 'text')

        #attribute css classes to widgets
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }





class CommentForm(forms.ModelForm):
    #set up fields for form
    class Meta():
        model = Comment 
        fields = ('author', 'text')

        #attribute css classes to widgets
        widgets ={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

