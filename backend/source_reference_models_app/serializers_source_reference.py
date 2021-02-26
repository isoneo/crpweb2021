from rest_framework import serializers, permissions
from .model_sources import *

class Src_tbl_deal_status_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_tbl_deal_status
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
# class Src_task_reviewer_serializer(serializers.ModelSerializer):
# 	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)
#
# 	class Meta:
# 		model = Src_task_reviewer
# 		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}

class Src_tbl_deal_seller_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_tbl_deal_seller
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
class Src_tbl_deal_source_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_tbl_deal_source
		fields = '__all__'


class Src_tbl_deal_type_serializer(serializers.ModelSerializer):
	class Meta:
		model = Src_tbl_deal_type
		fields = '__all__'

class Src_afe_type_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_afe_type
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
class Src_department_list_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_department_list
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
class Src_fund_list_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_fund_list
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
class Src_int_type_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_int_type
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}
class Src_payout_type_serializer(serializers.ModelSerializer):
	# gondor_user_details = serializers.SerializerMethodField(required=False, allow_null=True, read_only=True)

	class Meta:
		model = Src_payout_type
		fields = '__all__'
		# extra_kwargs = {'rcd_datetime': {'required': False, 'allow_null': True},}







