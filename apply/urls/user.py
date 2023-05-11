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

from django.urls import re_path
from apply import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from ganeti.forms import PickyAuthenticationForm

urlpatterns = [
    re_path(r'^info/(?P<type>\w+)/(?P<usergroup>[\w\.\@-]+)/?$', views.user_info, name="user-info"),
    re_path(r'^details/$', views.detail_api, name="user-details-json"),
    re_path(r'^idle/$', views.idle_accounts, name="idle_accounts"),
    re_path(r'^profile/$', views.profile, name="profile"),
    re_path(r'^mail_change/$', views.mail_change, name="mail-change"),
    re_path(r'^name_change/$', views.name_change, name="name-change"),
    re_path(r'^other_change/$', views.other_change, name="other-change"),
    re_path(r'^keys/$', views.user_keys, name="user-keys"),
    re_path(r'^keys/delete/(?P<key_id>\d+)?$', views.delete_key, name="delete-key"),
    re_path(r'^login/', LoginView.as_view(template_name='users/login.html',
                            authentication_form=PickyAuthenticationForm),
        name="login"),
    re_path(r'^logout/', LogoutView.as_view(next_page='/'), name="logout"),
    re_path(r'^pass_change/$', PasswordChangeView.as_view(template_name='users/pass_change.html'), name="pass_change"),
    re_path(r'^pass_change/done/$', PasswordChangeDoneView.as_view(template_name='users/pass_change_done.html'), name="password_change_done" ),
    re_path(r'^pass_change/notify/$', views.pass_notify, name="pass_change_notify"),
]
