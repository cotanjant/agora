from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

import agora
from agora import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # we add django's pre-made auth models
    # include() to include pre-made routes
    # we can include() our routes from agora/ for DRY (do not repeat yourself)
    # this line defines these routes:
    # 1. /accounts/login
    # 2. /accounts/signup
    # 3. /accounts/password_change
    # 4. /accounts/password_reset
    path('accounts/', include("django.contrib.auth.urls")),
    # now, we import urls from agora/ like i said we can do this
    # we say '' to create routes from agora/urls.py at root(/)
    path('', include("agora.urls"))
]
