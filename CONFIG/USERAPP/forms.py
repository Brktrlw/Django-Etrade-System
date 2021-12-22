from django import forms


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=50, label="Kullanıcı Adı", required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=150, label="Parola", required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["userName"].widget = forms.TextInput(
            attrs={"placeholder": "Kullanıcı Adını Giriniz", "class": "form-control form-control-lg"})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"placeholder": "Parolanızı Giriniz", "class": "form-control form-control-lg"})

class RegisterForm(forms.Form):
    userName = forms.CharField(max_length=50, label="Kullanıcı Adı", required=True)
    password = forms.CharField(max_length=150, label="Parola", required=True)
    confirm = forms.CharField(max_length=150, label="Parola Tekrarı", required=True)
    email = forms.CharField(max_length=200, label="Email", required=True)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["userName"].widget = forms.TextInput(
            attrs={"placeholder": "Kullanıcı Adı Giriniz", "class": "form-control form-control-lg"})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"placeholder": "Parola Giriniz", "class": "form-control form-control-lg"})
        self.fields["email"].widget = forms.EmailInput(
            attrs={"placeholder": "Email Adresi Giriniz", "class": "form-control form-control-lg"})
        self.fields["confirm"].widget = forms.PasswordInput(
            attrs={"placeholder": "Parolayı Tekrar Giriniz", "class": "form-control form-control-lg"})

    def clean(self):
        userName = self.cleaned_data.get("userName")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")

        if password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {"userName": userName, "password": password, "email": email}
        return values

