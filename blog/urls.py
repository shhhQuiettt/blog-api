from django.urls import path
from . import views as v


urlpatterns = [path("posts", v.CreateListPosts.as_view())]
