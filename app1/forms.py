from django import forms

from .models import question

class questionForm_text(forms.ModelForm):

    class Meta:
        model = question
        fields = ('Subject', 'Class', 'topic','difficulty','Question')

class questionForm_image(forms.ModelForm):

    class Meta:
        model = question
        fields = ('Subject', 'Class', 'topic','difficulty','Question_Image')

class inputForm(forms.ModelForm):

	class Meta:
		model = question
		fields = ('Class','Subject','topic','difficulty','Number_of_Questions')
