from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    duration = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    difficulty = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '60', 'rows': '6'}))
    img = forms.FileField()
