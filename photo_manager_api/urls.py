from django.urls import path
from .views import PhotoViewList, PhotoView, PhotoViewCreate

urlpatterns = [
    path('photos/', PhotoViewList.as_view()),
    path('photos/create/', PhotoViewCreate.as_view()),
    path('photos/<int:pk>', PhotoView.as_view()),
]
