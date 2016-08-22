from django import forms

from .models import Post

# We need to tell Django, that this form is a ModelForm (so Django will do
# some magic for us) - forms.ModelForm is responsible for that.
class PostForm(forms.ModelForm):

    # Class Meta tells Django which model should be used to create this form
    class Meta:
        model = Post
        fields = ('title', 'text',) # indicate which fields should end up in the form
