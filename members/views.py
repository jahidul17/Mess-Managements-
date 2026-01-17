from rest_framework import generics, permissions
from .models import MemberProfile
from .serializers import MemberProfileSerializer

class MemberCreateView(generics.CreateAPIView):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class MemberProfileView(generics.RetrieveAPIView):
    serializer_class = MemberProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.memberprofile
