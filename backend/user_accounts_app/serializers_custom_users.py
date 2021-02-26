from rest_framework import serializers, permissions
from .model_custom_user import Gondor_mgmt
from django.contrib.auth.models import User
from source_reference_models_app.serializers_source_reference import Src_department_list_serializer, Src_fund_list_serializer


class Gondor_mgmt_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Gondor_mgmt
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}


class custom_UserSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField()

	def get_full_name(self, obj):
		return obj.first_name + ' ' + obj.last_name
	class Meta:
		model= User
		fields = ('first_name','last_name','email','id','full_name',)
	def to_representation(self, instance):
		response = super(custom_UserSerializer, self).to_representation(instance)
		response['gondor_related'] = Gondor_mgmt_full_user_serializer(instance.gondor_to_user, many=False).data
		return response

class Gondor_mgmt_full_user_serializer(serializers.ModelSerializer):
	# rcd_user = custom_UserSerializer(source='rcd_user__gondor_to_user', many=False)
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)
	# email = serializers.ReadOnlyField(source='rcd_user.email')
	# full_name = serializers.SerializerMethodField()
	class Meta:
		model = Gondor_mgmt
		fields = ('related_user_fund','related_user_department')

		# extra_kwargs = {'gondor_to_user': {'required': False, 'allow_null': True},}
		# depth = 1
	# def get_gondor_user_details(self, obj):
	# 	print(obj)
	# 	user_detail_obj = obj.rcd_user
	# 	return custom_UserSerializer(user_detail_obj).data
	# def get_full_name(self, obj):
	# 	print(obj.gondor_to_user.get_full_name)
		# return obj.first_name + ' ' + obj.last_name
	def to_representation(self, instance):
		response = super(Gondor_mgmt_full_user_serializer, self).to_representation(instance)
		# print(instance.related_user_fund)
		response['related_user_fund'] = Src_fund_list_serializer(instance.related_user_fund, many=True).data
		response['related_user_department'] = Src_department_list_serializer(instance.related_user_department, many=True).data
		return response
		# print(instance.gondor_to_user.username)
		# print(User._meta.fields())
		# response['user_detail'] = custom_UserSerializer(instance.rcd_user).data

