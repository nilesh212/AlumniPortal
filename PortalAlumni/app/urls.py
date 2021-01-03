from django.conf.urls import url
from app import views

#template name
app_name='app'

urlpatterns=[
    url(r'^signup/',views.signup,name='signup'),
    url(r'^$',views.base,name='base'),
    url(r'^(?P<pk>\d+)/post/new/$',views.post_form,name='post_new'),
    url(r'^(?P<pk>\d+)/post/detail/$',views.postdetail,name='post_detail'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^(?P<pk>\d+)/event/forms/$',views.event_form,name='event_form'),
    url(r'^(?P<pk>\d+)/event/detail/$',views.event_detail,name='event_detail'),


]


#url(r'^post_form/',views.post_form,name='post_form'),