from django import forms
from .models import Users, Disease


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['cname'].empty_label = "Select"
        
class DiseaseForm(forms.ModelForm):

    class Meta:
        model = Disease
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DiseaseForm,self).__init__(*args, **kwargs)
        self.fields['cname'].empty_label = "Select"

  
    