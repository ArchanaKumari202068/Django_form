from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name ", max_length=100,error_messages={
#         "required": "Your name must not be empty",
#         "max_length":"Please enter a shorter name!"
#     })

#     review_text = forms.CharField(label="your Feedback", widget= forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # if want to add all field like user_name, rating ,review_text... so use __all__
        fields='__all__'
        # exclude = ['owner_comment']
        labels={
            "user_name" :"Your Name",
            "review_text" : "Your Feedback",
            "rating":" Your Rating"
        }
        error_messages = {
            "user_name" :{
                "required":"Your name must not be empty",
                "max_length":" Please enter a shorter name!"
            }
        }
