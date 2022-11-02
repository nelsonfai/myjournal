
from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Articles,Writeups,Comments

class ArticleForm (ModelForm):
  
    class Meta:
        model=Articles
        fields=('title','body','tags','status')
       
    def __init__(self,*args,**kwargs):
            super(ArticleForm,self).__init__(*args,**kwargs)

            self.fields['title'].widget.attrs['class']='form_control'
            self.fields['title'].widget.attrs['placeholder']='Enter Tilte'
            self.fields['status'].widget.attrs['class']='form_control'
            self.fields['body'].widget.attrs['class']='form_control2'
            self.fields['body'].widget.attrs['placeholder']='Enter text message here'
            self.fields['tags'].widget.attrs['class']='form_control'
            self.fields['tags'].widget.attrs['placeholder']='e.g science,meditation,marriage,self-reflection'

class UpdateForm (ModelForm):
  
    class Meta:
        model=Articles
        fields=('title','body','tags','status')
       
    def __init__(self,*args,**kwargs):
            super(ArticleForm,self).__init__(*args,**kwargs)

            self.fields['title'].widget.attrs['class']='form_control'
            self.fields['title'].widget.attrs['placeholder']='Enter Tilte'
            self.fields['status'].widget.attrs['class']='form_control'
            self.fields['body'].widget.attrs['class']='form_control2'
            self.fields['body'].widget.attrs['placeholder']='Enter text message here'
            self.fields['tags'].widget.attrs['class']='form_control'
            self.fields['tags'].widget.attrs['placeholder']='e.g science,meditation,marriage,self-reflection'


class WriteupForm(ModelForm):
    class Meta:
        model = Writeups
        fields = ('title','body')
    def __init__(self,*args,**kwargs):
            super(WriteupForm,self).__init__(*args,**kwargs)

            self.fields['title'].widget.attrs['class']='form_control'
            self.fields['title'].widget.attrs['placeholder']='Enter a title (optional)'
            self.fields['body'].widget.attrs['class']='form_control'
            self.fields['body'].widget.attrs['placeholder']='Write here ....'

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
    def __init__(self,*args,**kwargs):
            super(CommentForm,self).__init__(*args,**kwargs)

            self.fields['comment'].widget.attrs['class']='form_control'
            self.fields['comment'].widget.attrs['placeholder']='Enter Comment here'
           