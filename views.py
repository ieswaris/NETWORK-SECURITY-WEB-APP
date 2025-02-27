from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from .models import UserPredictModel
from .forms import UserPredictDataForm



def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


Model = joblib.load('C:/Users/eswar/Music/ITPML03-FINAL CODING/Deploy/users/CYBER1.pkl')
def Deploy_8(request):
    if request.method == 'POST':
        form = UserPredictDataForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from form
                flow_duration=form.cleaned_data['flow_duration'],
                fwd_pkts_tot=form.cleaned_data['fwd_pkts_tot'],
                bwd_pkts_tot=form.cleaned_data['bwd_pkts_tot'],
                fwd_data_pkts_tot=form.cleaned_data['fwd_data_pkts_tot'],
                bwd_data_pkts_tot=form.cleaned_data['bwd_data_pkts_tot'],
                fwd_pkts_per_sec=form.cleaned_data['fwd_pkts_per_sec'],
                bwd_pkts_per_sec=form.cleaned_data['bwd_pkts_per_sec'],
                flow_pkts_per_sec=form.cleaned_data['flow_pkts_per_sec'],
                down_up_ratio=form.cleaned_data['down_up_ratio'],
                fwd_header_size_tot=form.cleaned_data['fwd_header_size_tot'],
                fwd_header_size_min=form.cleaned_data['fwd_header_size_min'],
                fwd_header_size_max=form.cleaned_data['fwd_header_size_max'],
                bwd_header_size_tot=form.cleaned_data['bwd_header_size_tot'],
                bwd_header_size_min=form.cleaned_data['bwd_header_size_min'],
                bwd_header_size_max=form.cleaned_data['bwd_header_size_max'],
                flow_FIN_flag_count=form.cleaned_data['flow_FIN_flag_count'],
                flow_SYN_flag_count=form.cleaned_data['flow_SYN_flag_count'],
                flow_RST_flag_count=form.cleaned_data['flow_RST_flag_count'],
                fwd_PSH_flag_count=form.cleaned_data['fwd_PSH_flag_count'],
                bwd_PSH_flag_count=form.cleaned_data['bwd_PSH_flag_count'],
                flow_ACK_flag_count=form.cleaned_data['flow_ACK_flag_count'],
                fwd_URG_flag_count=form.cleaned_data['fwd_URG_flag_count'],
                bwd_URG_flag_count=form.cleaned_data['bwd_URG_flag_count'],
                flow_CWR_flag_count=form.cleaned_data['flow_CWR_flag_count'],
                flow_ECE_flag_count=form.cleaned_data['flow_ECE_flag_count'],
                fwd_pkts_payload_min=form.cleaned_data['fwd_pkts_payload_min'],
                fwd_pkts_payload_max=form.cleaned_data['fwd_pkts_payload_max'],
                fwd_pkts_payload_tot=form.cleaned_data['fwd_pkts_payload_tot'],
                fwd_pkts_payload_avg=form.cleaned_data['fwd_pkts_payload_avg'],
                fwd_pkts_payload_std=form.cleaned_data['fwd_pkts_payload_std'],
                bwd_pkts_payload_min=form.cleaned_data['bwd_pkts_payload_min'],
                bwd_pkts_payload_max=form.cleaned_data['bwd_pkts_payload_max'],
                bwd_pkts_payload_tot=form.cleaned_data['bwd_pkts_payload_tot'],
                bwd_pkts_payload_avg=form.cleaned_data['bwd_pkts_payload_avg'],
                bwd_pkts_payload_std=form.cleaned_data['bwd_pkts_payload_std'],
                flow_pkts_payload_min=form.cleaned_data['flow_pkts_payload_min'],
                flow_pkts_payload_max=form.cleaned_data['flow_pkts_payload_max'],
                flow_pkts_payload_tot=form.cleaned_data['flow_pkts_payload_tot'],
                flow_pkts_payload_avg=form.cleaned_data['flow_pkts_payload_avg'],
                flow_pkts_payload_std=form.cleaned_data['flow_pkts_payload_std'],
                fwd_bulk_packets=form.cleaned_data['fwd_bulk_packets'],
                bwd_bulk_packets=form.cleaned_data['bwd_bulk_packets'],
                fwd_bulk_rate=form.cleaned_data['fwd_bulk_rate'],
                bwd_bulk_rate=form.cleaned_data['bwd_bulk_rate'],
                fwd_init_window_size=form.cleaned_data['fwd_init_window_size'],
                bwd_init_window_size=form.cleaned_data['bwd_init_window_size'],
                fwd_last_window_size=form.cleaned_data['fwd_last_window_size'],
                
                # Prepare features for prediction
                features = np.array([[flow_duration,fwd_pkts_tot,bwd_pkts_tot,fwd_data_pkts_tot,bwd_data_pkts_tot,
                                      fwd_pkts_per_sec,bwd_pkts_per_sec,flow_pkts_per_sec,down_up_ratio,fwd_header_size_tot,
                                      fwd_header_size_min,fwd_header_size_max,bwd_header_size_tot,bwd_header_size_min,bwd_header_size_max,
                                      flow_FIN_flag_count,flow_SYN_flag_count,flow_RST_flag_count,fwd_PSH_flag_count,bwd_PSH_flag_count,
                                      flow_ACK_flag_count,fwd_URG_flag_count,bwd_URG_flag_count,flow_CWR_flag_count,flow_ECE_flag_count,
                                      fwd_pkts_payload_min,fwd_pkts_payload_max,fwd_pkts_payload_tot,fwd_pkts_payload_avg,fwd_pkts_payload_std,
                                      bwd_pkts_payload_min,bwd_pkts_payload_max,bwd_pkts_payload_tot,bwd_pkts_payload_avg,bwd_pkts_payload_std,
                                      flow_pkts_payload_min,flow_pkts_payload_max,flow_pkts_payload_tot,flow_pkts_payload_avg,
                                      flow_pkts_payload_std,fwd_bulk_packets,bwd_bulk_packets,fwd_bulk_rate,bwd_bulk_rate,
                                      fwd_init_window_size,bwd_init_window_size,fwd_last_window_size
                                    ]])
                # Predict using the loaded model
                features=features.reshape(1,-1)
                prediction = Model.predict(features)
                prediction = prediction[0]
                print(prediction)
                # # Determine the result based on prediction
                # attack = ['DOS_SYN_Hping','Thing_Speak','ARP_poisioning','MQTT_Publish','NMAP_UDP_SCAN','NMAP_XMAS_TREE_SCAN',
                #          'NMAP_OS_DETECTION','MAP_TCP_scan','DDOS_Slowloris','Wipro_bulb','Metasploit_Brute_Force_SSH','NMAP_FIN_SCAN',
                #         ]
                # result = attack[prediction]
                if prediction == 0:
                    result= 'ARP_poisioning'    
                elif prediction == 1:
                    result='DDOS_Slowloris'
                elif prediction == 2:
                    result='DOS_SYN_Hping' 
                elif prediction == 3:
                    result='Metasploit_Brute_Force_SSH'
                elif prediction == 4:
                    result='MQTT_Publish'
                elif prediction == 5:
                    result ='NMAP_FIN_SCAN'
                elif prediction == 6:
                    result = 'NMAP_OS_DETECTION'
                elif prediction == 7:
                    result='NMAP_TCP_scan' 
                elif prediction == 8:
                    result='NMAP_UDP_SCAN'
                elif prediction == 9:
                    result = 'NMAP_XMAS_TREE_SCAN'
                elif prediction == 10:
                    result ='Thing_Speak'
                elif prediction == 11:
                    result ='Wipro_bulb'     
                
                # Save data to database
                instance = form.save(commit=False)
                instance.label = result
                instance.save()
                
                # Render output page with prediction result
                return render(request, 'app/output.html', {'result': result})
    else:
        form = UserPredictDataForm()
    
    return render(request, 'app/deploy_8.html', {'form': form})




import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
from django.shortcuts import render





def Basic_report(request):
    return render(request,'app/Basic_report.html')

def Metrics_report(request):
    return render(request,'app/Metrics_report.html')


def Crop(request):
    data = UserPredictModel.objects.all()
    return render(request, 'app/network_db.html', {'data': data})




def logout_view(request):  
    auth_logout(request)
    return redirect('/')


