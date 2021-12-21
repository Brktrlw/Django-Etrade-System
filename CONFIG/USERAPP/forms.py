from django import forms

class LoginForm(forms.Form):
    userName = forms.CharField(max_length=50,label="Kullanıcı Adı",required=True)
    password = forms.CharField(widget=forms.PasswordInput,max_length=150,label="Parola",required=True)

    def __init__(self,*args,**kwargs):
       super(LoginForm, self).__init__(*args, **kwargs)
       self.fields["userName"].widget=forms.TextInput(attrs={"placeholder":"Kullanıcı Adını Giriniz","class":"form-control form-control-lg"})
       self.fields["password"].widget=forms.PasswordInput(attrs={"placeholder":"Parolanızı Giriniz","class":"form-control form-control-lg"})
