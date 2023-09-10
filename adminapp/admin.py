from django.contrib import admin
from . models import Booking,News, mBooking

# Register your models here.
admin.site.register(Booking)
admin.site.register(News)
admin.site.register(mBooking)