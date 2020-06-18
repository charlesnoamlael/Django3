from django.contrib import admin
from django.urls import include, path
from .views import hello_world
from .views import vai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('ola/', vai),
    path('blog/', include('website.urls')), # 'blog/' = pode charmar do que quiser
]
