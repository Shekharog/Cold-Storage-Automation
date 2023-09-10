from django.contrib import admin
from . models import FarmerInfo,MerchantInfo,LoginInfo,Enquiry
#enter your modles
admin.site.register(FarmerInfo)
admin.site.register(MerchantInfo)
admin.site.register(LoginInfo)
admin.site.register(Enquiry)
