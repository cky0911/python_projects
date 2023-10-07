from django import forms


class MyRegForm(forms.Form):
    username = forms.CharField(label='用户名')
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    username2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    def clean_username(self):
        uname = self.cleaned_data['username']
        if len(uname) < 2:
            raise forms.ValidationError('username too short')
        return uname

    # def clean_password1(self):
    #     pwd1 = self.cleaned_data['password1']
    #     if len(pwd1) == 0:
    #         raise forms.ValidationError('password can not be empty')
    #     return pwd1

    def clean(self):
        pwd1 = self.cleaned_data['password1']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('The two password entries are inconsistent')
        return self.cleaned_data
