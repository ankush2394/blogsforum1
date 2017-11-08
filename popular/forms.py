from django.forms import ModelForm
from add_blog.models import Comment
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
                "text"
                  ]
