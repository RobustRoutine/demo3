from django.forms import ModelForm
from .models import User
from .models import teacher_timetable

class teacher_timetableform(ModelForm):
    class Meta:
        model=teacher_timetable
        fields='__all__'


class UserForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'