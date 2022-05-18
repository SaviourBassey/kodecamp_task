from django.urls import path
from .views import home, about, contact


urlpatterns = [
    path("", home), #A
    path("about-me/for-me/for-us/", about), #B
    path("contact-me/", contact) #C
]

hsdfsdfs

hjsdbvfjbsbf