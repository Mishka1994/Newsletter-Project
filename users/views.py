from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, FormView, TemplateView, ListView

from users.forms import UserRegisterForm, UserProfileForm, UserForm
from users.models import User


class RegisterView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:email_verify_sended')

    def form_valid(self, form):
        if form.is_valid():
            current_date = get_current_site(self.request)
            new_user = form.save()
            code = default_token_generator.make_token(new_user)
            new_user.code_for_verify = code
            new_user.save()
            context = {
                'token': code,
                'domain': current_date.domain,
            }
            send_mail(
                subject='Ссылка для верификации почты',
                message=render_to_string('users/email_verify_message.html', context),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{new_user}']
            )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    models = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class VerifyTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/email_verify_sended'


class EmailVerifyUnsuccessful(View):
    model = User
    template_name = 'users/email_verify_unsuccessful'


class UserListView(UserPassesTestMixin, ListView):
    model = User
    form_class = UserForm

    def test_func(self):
        return self.model.is_staff


def is_active_setting_for_stuff(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
        user.save()
        return redirect(reverse('users:list_user'))
    else:
        user.is_active = True
        user.save()
        return redirect(reverse('users:list_user'))


def verify_email_page(request, token):
    template_name = 'users/email_verify_done.html'
    unsuccessful_template_name = 'users/email_verify_unsuccessful.html'
    new_user = User.objects.get(code_for_verify=token)
    if new_user:
        new_user.is_active = True
        new_user.save()
        return render(request, template_name)
    else:
        return render(request, unsuccessful_template_name)
