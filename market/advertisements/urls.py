from django.urls import path

from . import views


urlpatterns = [
    path('',
         views.AdvertList.as_view(),
         name='advert_list'),

    path('advert_create',
         views.AdvertCreate.as_view(),
         name='advert_create'),

    path('advert_<int:pk>',
         views.AdvertDetail.as_view(),
         name='advert_detail'),

    path('advert_<int:pk>/edit',
         views.AdvertUpdate.as_view(),
         name='advert_edit'),

    path('advert_<int:pk>/delete',
         views.AdvertDelete.as_view(),
         name='advert_delete'),

    path('advert_<int:pk>/reply',
         views.ReplyCreate.as_view(),
         name='reply_create'),

    path('reply_<int:pk>_accept',
         views.ReplyAccept.as_view(),
         name='reply_accept'),

    path('reply_<int:pk>_delete',
         views.ReplyDelete.as_view(),
         name='reply_delete'),

    path('my',
         views.ReplyList.as_view(),
         name='my'),
]
