from django.urls import path, include

urlpatterns = [
    path('api/', include('crowdfund.api.urls'))
]