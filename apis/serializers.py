from rest_framework.serializers import ModelSerializer
from basetables import models

class CustomerSerializer(ModelSerializer):
    class Meta:
        model=models.Customer
        fields='__all__'
        read_only_fields = ('approved_limit',)
    
    def create(self,validated_data):
        validated_data.pop('customer_id', None)
        monthly_income = validated_data.get('monthly_income')
        approved_limit = round((36 * monthly_income) / 100000) * 100000
        return models.Customer.objects.create(approved_limit=approved_limit,**validated_data)
    
    def to_representation(self, instance):
        return {
            'customer_id': instance.customer_id,
            'name': f"{instance.first_name} {instance.last_name}",
            'age': instance.age,
            'monthly_income': int(instance.monthly_income),
            'approved_limit': int(instance.approved_limit),
            'phone_number': int(instance.phone_number)
        }
    
class LoanSerializer(ModelSerializer):
    class Meta:
        model = models.Loan
        fields = '__all__'
        # read_only_fields = ('loan_id',)

    def create(self, validated_data):
        validated_data.pop('loan_id', None)
        return models.Loan.objects.create(**validated_data)
    
    def to_representation(self, instance):
        return {
            "loan_id": instance.loan_id,
            "customer_id": instance.customer_id.customer_id,
            "loan_approved": True,
            "message": "Loan approved",
            "monthly_installment": round(instance.monthly_installment, 2)
        }

class LoanViewSerializer(ModelSerializer):
    customer_id = CustomerSerializer()
    class Meta:
        model = models.Loan
        fields = ['loan_id','customer_id','loan_amount','interest_rate','monthly_installment','tenure']

class AllLoanViewSerializer(ModelSerializer):
    class Meta:
        model = models.Loan
        fields = ['loan_id', 'loan_amount', 'interest_rate', 'monthly_installment', 'tenure', 'emis_paid_on_time']

    def to_representation(self, instance):
        repayments_left = max(instance.tenure - instance.emis_paid_on_time, 0)
        return {
            "loan_id": instance.loan_id,
            "loan_amount": instance.loan_amount,
            "interest_rate": instance.interest_rate,
            "monthly_installment": round(instance.monthly_installment, 2),
            "repayments_left": repayments_left
        }