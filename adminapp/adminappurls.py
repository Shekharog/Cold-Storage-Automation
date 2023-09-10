from django.urls import path
from . import views
urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('enquiries/',views.enquiries,name='enquiries'),
    path('booking/',views.booking,name='booking'),
    path('mbooking/',views.mbooking,name='mbooking'),
    path('purchase/',views.purchase,name='purchase'),
    path('mac/',views.mac,name='mac'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('book/(?p<ano>\w+)',views.book,name='book'),
    path('mbook/(?p<m>\w+)',views.mbook,name='mbook'),
    path('pbook/',views.pbook,name='pbook'),
    path('mlook/',views.mlook,name='mlook'),
    path('viewbook/(?p<ano>\w+)',views.viewbook,name='viewbook'),
    path('mview/(?p<m>\w+)',views.mview,name='mview'),
    path('deleteenq/(?p<id>\d+)',views.deleteenq,name='deleteenq'),
    path('addnews/',views.addnews,name='addnews'),
    path('deletenews/(?p<id>\d+)',views.deletenews,name='deletenews'),
    path('changepwd/',views.changepwd,name='changepwd'),
    path('pay/(?p<ano>\w+)',views.pay,name='pay'),
    path('paid/',views.paid,name='paid'),
    path('macpay/(?p<mc>\w+)',views.macpay,name='macpay'),
    path('mpaid/',views.mpaid,name='mpaid')

]