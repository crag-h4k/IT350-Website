from django import forms

class UserForm(form.ModelForm):
	class Meta:
		model = User
		widget = {
		'password': forms.PasswordInput(),
	}
