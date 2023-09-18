# -*- coding: utf-8 -*- vim:fileencoding=utf-8:
# Copyright (C) 2010-2014 GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail as _RegistrationForm
from apply.models import Organization
from captcha.fields import ReCaptchaField


class RegistrationForm(_RegistrationForm):
    name = forms.CharField()
    surname = forms.CharField()
    phone = forms.CharField(required=False)
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        required=False,
        label=_("Organization")
    )
    if settings.RECAPTCHA_PRIVATE_KEY and settings.RECAPTCHA_PUBLIC_KEY:
        recaptcha = ReCaptchaField()


class PasswordResetFormPatched(PasswordResetForm):
    error_messages = {
        'unknown': _("That e-mail address doesn't have an associated "
                     "user account or the account has not been activated yet. Are you sure you've registered?"),
        'unusable': _("The user account associated with this e-mail "
                      "address cannot reset the password."),
    }
