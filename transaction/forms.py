from django import forms
from django.contrib.auth.models import User
from .models import MerchantSetTransact, MerchantCommssion, SubscriberTransact, TransactionComplete



class MerchantTransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = MerchantCommssion
        exclude = ('payment_confirm','transaction')
        

# setting of transaction
class MerchantSetTransactForm(forms.ModelForm):
   
    class Meta:
        
        model = MerchantSetTransact
        fields = ('max_amount', 'min_amount', 'prefered_method', 'current_location', 'remote_option')
        # exclude = ('max_amount','min_amount', 'prefered_method', '')
        # widgets = {
        #     'comment': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        # }

# Comment on Transaction
class SubscriberTransactForm(forms.ModelForm):
    class Meta:
        model = SubscriberTransact
        fields = ('trans_amount', 'payment_method', 'delivery_method',)



class TransactionForm(forms.ModelForm):   
    class Meta:
        model = MerchantSetTransact
        fields = ('max_amount', 'min_amount',)
     

class CommentForm(forms.ModelForm):
    class Meta:
        model = SubscriberTransact
        fields = ('trans_amount', 'current_location',)



class ReplyForm(forms.ModelForm):
    class Meta:
        model = TransactionComplete
        fields = ('remark', 'trans_success',)
