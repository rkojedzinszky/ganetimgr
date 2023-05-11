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

from django.conf.urls import url
from apply import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from ganeti.forms import PickyAuthenticationForm

urlpatterns = [
    url(r'^info/(?P<type>\w+)/(?P<usergroup>[\w\.\@-]+)/?$', views.user_info, name="user-info"),
    url(r'^details/$', views.detail_api, name="user-details-json"),
    url(r'^idle/$', views.idle_accounts, name="idle_accounts"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^mail_change/$', views.mail_change, name="mail-change"),
    url(r'^name_change/$', views.name_change, name="name-change"),
    url(r'^other_change/$', views.other_change, name="other-change"),
    url(r'^keys/$', views.user_keys, name="user-keys"),
    url(r'^keys/delete/(?P<key_id>\d+)?$', views.delete_key, name="delete-key"),
    url(r'^login/', LoginView.as_view(template_name='users/login.html',
                            authentication_form=PickyAuthenticationForm),
        name="login"),
    url(r'^logout/', LogoutView.as_view(next_page='/'), name="logout"),
    url(r'^pass_change/$', PasswordChangeView.as_view(template_name='users/pass_change.html'), name="pass_change"),
    url(r'^pass_change/done/$', PasswordChangeDoneView.as_view(template_name='users/pass_change_done.html'), name="password_change_done" ),
    url(r'^pass_change/notify/$', views.pass_notify, name="pass_change_notify"),
]
