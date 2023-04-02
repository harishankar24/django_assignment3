from django.forms import ModelForm, Textarea
from .models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 10}),
        }
        labels = {
            'cname': ('Course Name'),
        }