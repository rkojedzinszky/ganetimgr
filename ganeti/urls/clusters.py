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
from ganeti import views

urlpatterns = [
    # this view lives in jobs.py
    re_path(r'^jobdetails/?$', views.job_details, name="jobdets-popup"),
    re_path(r'^popup/?', views.instance_popup, name="instance-popup"),
    re_path(r'^nodes/$', views.get_clusternodes, name="cluster-nodes"),
    re_path(r'^nodes/pjax/$', views.get_clusternodes_pjax, name="cluster-nodes-pjax"),
    re_path(r'^jnodes/(?P<cluster>[0-9]+)/$', views.clusternodes_json, name="cluster-nodes-json"),
    re_path(r'^jnodes/$', views.clusternodes_json, name="cluster-nodes-json"),
    re_path(r'^instance/destreinst/(?P<application_hash>\w+)/(?P<action_id>\d+)/$', views.reinstalldestreview, name='reinstall-destroy-review'),
    re_path(r'^detail/$', views.clusterdetails, name="clusterdetails"),
    re_path(r'^detail/json/$', views.clusterdetails_json, name="clusterdetails_json"),

]
