# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Hero
from .models import KibbutzStory, NovaPartyTestimony, Testimonial, AbducteeTestimony, Comment, Candle
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Call the parent method to handle the default validation
        super().confirm_login_allowed(user)
        # Check if the user is active. If not, raise a validation error with a custom message
        if not user.is_active:
            raise forms.ValidationError(
                "הסיסמא שגויה, נא לנסות שוב",  # Custom error message
                code='invalid_login'  # Error code
            )
        
class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['first_name', 'last_name', 'age', 'hometown', 'country_of_birth', 'hero_story', 'image']
        labels = {
            'first_name': 'שם פרטי',  
            'last_name': 'שם משפחה',
            'age': 'גיל',
            'hometown': 'עיר מגורים',
            'country_of_birth': 'ארץ לידה',
            'hero_story': 'סיפור גבורה',
            'image': 'תמונה', 
        }
        widgets = {
            'image': forms.FileInput()  # Use FileInput for single file uploads
        }

class KibbutzStoryForm(forms.ModelForm):
    class Meta:
        model = KibbutzStory
        fields = ['title', 'content']
        labels = {
            'title': 'שם הקיבוץ',
            'content': 'סיפור הקיבוץ בעקבות המלחמה',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class NovaPartyTestimonyForm(forms.ModelForm):
    class Meta:
        model = NovaPartyTestimony
        fields = ['owner', 'story']
        labels = {
            'owner': 'בעל העדות',
            'story': 'סיפור העדות ממסיבת הנובה',
        }
        widgets = {
            'story': forms.Textarea(attrs={'rows': 5}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'story']
        labels = {
            'author': 'מחבר',
            'story': 'סיפור',
        }
        widgets = {
            'story': forms.Textarea(attrs={'rows': 5}),
        }

class AbducteeTestimonyForm(forms.ModelForm):
    class Meta:
        model = AbducteeTestimony
        fields = ['owner', 'story', 'age', 'date_of_return', 'image']
    owner = forms.CharField(label="שם החטוף המשוחרר", max_length=100)
    story = forms.CharField(label="מידע על אירועי השבי", widget=forms.Textarea)
    age = forms.IntegerField(label="גיל החטוף המשוחרר", required=True)
    date_of_return = forms.DateField(label="תאריך חזרה משבי", widget=forms.SelectDateWidget(years=range(1900, 2100)))
    image = forms.ImageField(label="תמונת החטוף ", required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'כתוב את התגובה שלך...'}),
        }
        labels = {
            'content': '',
        }

class CandleForm(forms.ModelForm):
    class Meta:
        model = Candle
        fields = ['name', 'message']
        labels = {
            'name': 'הדלקת נר לזכר',
            'message': 'כמה מילים לזכרו',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

