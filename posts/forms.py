from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        # fields = '__all__'
        # exclude= ('author', 'date_created')
        # widgets={
        #     "body": Textarea()
        # }