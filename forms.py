from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import UserPredictModel

from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']



class UserPredictDataForm(forms.ModelForm):
    class Meta:
        model = UserPredictModel
        fields =['flow_duration','fwd_pkts_tot','bwd_pkts_tot','fwd_data_pkts_tot','bwd_data_pkts_tot','fwd_pkts_per_sec','bwd_pkts_per_sec',
                  'flow_pkts_per_sec','down_up_ratio','fwd_header_size_tot','fwd_header_size_min','fwd_header_size_max','bwd_header_size_tot',
                  'bwd_header_size_min','bwd_header_size_max','flow_FIN_flag_count','flow_SYN_flag_count','flow_RST_flag_count','fwd_PSH_flag_count',
                  'bwd_PSH_flag_count','flow_ACK_flag_count','fwd_URG_flag_count','bwd_URG_flag_count','flow_CWR_flag_count','flow_ECE_flag_count',
                  'fwd_pkts_payload_min','fwd_pkts_payload_max','fwd_pkts_payload_tot','fwd_pkts_payload_avg','fwd_pkts_payload_std','bwd_pkts_payload_min',
                  'bwd_pkts_payload_max','bwd_pkts_payload_tot','bwd_pkts_payload_avg','bwd_pkts_payload_std','flow_pkts_payload_min','flow_pkts_payload_max',
                  'flow_pkts_payload_tot','flow_pkts_payload_avg','flow_pkts_payload_std','fwd_bulk_packets','bwd_bulk_packets','fwd_bulk_rate',
                  'bwd_bulk_rate','fwd_init_window_size','bwd_init_window_size','fwd_last_window_size',
                ]
