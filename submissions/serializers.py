from rest_framework import serializers, viewsets, permissions, routers
from .models import Hackathon, Submission, HackathonRegistration
from django.contrib.auth.models import User

# serializer for hackathon
class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['id', 'title', 'description', 'background_image', 'hackathon_image', 'submission_type', 'start_date', 'end_date', 'reward_prize']
    

# serializer for submission
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'name', 'summary', 'submission_file', 'submission_image', 'submission_link', 'hackathon']

    # modifying init so that user can make submissions only in the enrolled hackathons
    def __init__(self, *args, **kwargs):
        user = kwargs['context']['request'].user
        super().__init__(*args, **kwargs)
        self.fields['hackathon'].queryset = Hackathon.objects.filter(
            pk__in = HackathonRegistration.objects.filter(
            user = user
        ).values_list('hackathon', flat=True))

    def create(self, validated_data):
        hackathon = validated_data.get('hackathon')
        naming = {"file" : 'submission_file', "image" : "submission_image", "link" : "submission_link"}
        print(validated_data)
        if(validated_data.get(naming[hackathon.submission_type]) in (None, '') ):
            raise serializers.ValidationError("Submission type doesn't match the hackathon requirements.")

        submission = Submission.objects.create(**validated_data)
        return submission
        
# serializer for user submission
class SubmissionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

# serializer for user registrations
class HackathonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonRegistration
        fields = ['hackathon']