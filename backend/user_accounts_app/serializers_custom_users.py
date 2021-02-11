from rest_framework import serializers, permissions
from .model_custom_user import Gondor_mgmt

class Gondor_mgmt_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Gondor_mgmt
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}




