from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "autocomplete": "off",
                "placeholder": "Password"
            }
        )
    )