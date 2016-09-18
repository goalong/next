from django import forms
from django.contrib.auth import login as auth_login, get_user_model, authenticate
from django.urls import reverse


class SignInForm(forms.Form):

    error_messages = {
        'invalid_login': ('email or password wrong'),
        'inactive': ("This account is inactive."),
        'password_error': ('password error'),
        'no_cookies': ('no cookies'),
    }

    next = forms.CharField(required=False, widget=forms.HiddenInput())

    name = forms.CharField(
        label=('Name'),
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ('Name')}),

    )
    password = forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': ('Password')}),


    )

    def __init__(self, request, *args, **kwargs):

        self.request = request
        self.user_cache = None

        super(SignInForm, self).__init__(*args, **kwargs)
        UserModel = get_user_model()

        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if not self.fields['name'].label:
            self.fields['name'].label = self.username_field.verbose_name
    def clean(self):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        self.next_url = self.cleaned_data.get('next')

        if name and password:
            self.user_cache = authenticate(username=name,
                                           password=password)

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login']
                )
            # elif self.user_cache.is_active == GKUser.remove:
            #     raise forms.ValidationError(
            #         self.error_messages['inactive'],
            #         code='inactive',
            #     )

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(
                self.error_messages['no_cookies']
            )

    def login(self):
        auth_login(self.request, self.user_cache)
        # pass

    def get_next_url(self):

        if self.next_url:
            return self.next_url
        return reverse('web_selection')

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
