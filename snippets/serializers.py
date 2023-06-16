from rest_framework import serializers

from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    class Meta:
        model = Snippet
        fields = '__all__'
        require_fields = ['code',]
