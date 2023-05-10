from django.utils import timezone
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Hackathon, Submission, HackathonRegistration
from .serializers import (
    HackathonSerializer, SubmissionSerializer, HackathonRegistrationSerializer,
    SubmissionViewSerializer
)
from .permissions import IsAuthorizedToAddHackathons

# view for creating hackathons
class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthorizedToAddHackathons]

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(Q(start_date__lte=timezone.now()) | Q(end_date__lte=timezone.now()))
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# view for submitting
class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)

# view for listing all hackathons
class PublicHackathonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


# view for registering to a hackathon
class HackathonRegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HackathonRegistrationSerializer

    def get_queryset(self):
        return HackathonRegistration.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# view for viewing enrolled hackathons
class EnrolledHackathonViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        enrolled_hackathons = HackathonRegistration.objects.filter(user=request.user).values_list('hackathon', flat=True)
        hackathons = Hackathon.objects.filter(pk__in=enrolled_hackathons)
        serializer = HackathonSerializer(hackathons, many=True)
        return Response(serializer.data)

# view for viewing user's submissions
class UserSubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubmissionViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hackathon_id = self.kwargs.get('hackathon_id')
        return Submission.objects.filter(hackathon__id=hackathon_id, user=self.request.user)

# view for viewing Users who are enrolled in at least one hackathon
class EnrolledParticipantViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthorizedToAddHackathons]
    def list(self, request):
        enrolled_users = HackathonRegistration.objects.values_list('user', flat=True).distinct()
        users = User.objects.filter(id__in=enrolled_users)
        return Response(users.values('id', 'username', 'email'))

# view for viewing users who are not enrolled even in a single hackathon
class NonEnrolledParticipantViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthorizedToAddHackathons]
    def list(self, request):
        enrolled_users = HackathonRegistration.objects.values_list('user', flat=True).distinct()
        users = User.objects.exclude(id__in=enrolled_users)
        return Response(users.values('id', 'username', 'email'))