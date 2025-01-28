from django import forms
from.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name":"Your Name",
            "user_email":"Your Email",
            "text":"Your Comment",      
            }
        error_messages = {
            "user_name":{
                "required":"Please Enter Your Name",
                "max_length":"Name Cannot Exceed 100 Characters",
            },
            "user_email":{
                "required":"Please Enter Your Email Address",
                "invalid":"Please Enter a Goddamn Valid Email",
                "max_length":"what kind of email is this long?",
            }
        }
        widgets = {
            "user_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "user_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your comment", "rows": 4}),
        }