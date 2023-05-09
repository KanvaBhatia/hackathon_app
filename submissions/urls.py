from django.urls import path, include
from rest_framework import routers
from .views import (
        HackathonViewSet, SubmissionViewSet, EnrolledHackathonViewSet,
        UserSubmissionViewSet, PublicHackathonViewSet, HackathonRegistrationViewSet
)
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView,
    PasswordChangeView, UserDetailsView, PasswordResetConfirmView,
    PasswordResetView, PasswordChangeView
)

router = routers.DefaultRouter()
router.register(r'create-hackathon', HackathonViewSet, basename = 'hackathons')
router.register(r'hackathons', PublicHackathonViewSet, basename='all-hackathons')
router.register(r'register', HackathonRegistrationViewSet, basename='register-hackathons')
router.register(r'submit', SubmissionViewSet, basename = 'submit')
router.register(r'enrolled-hackathons', EnrolledHackathonViewSet, basename='enrolled-hackathons')
router.register(r'hackathons/(?P<hackathon_id>\d+)/user-submissions', UserSubmissionViewSet, basename='user-submissions')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/password/reset/', PasswordResetView.as_view(),
            name='rest_password_reset'),
    path('auth/password/reset/confirm/<uidb64>/<token>/',
            PasswordResetConfirmView.as_view(),
            name='rest_password_reset_confirm'),
    path('auth/password/change/', PasswordChangeView.as_view(),
            name='rest_password_change'),
    path('auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('auth/', include('dj_rest_auth.urls')),
]
