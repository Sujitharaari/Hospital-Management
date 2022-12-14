from django.contrib import admin
from . models import Departments, Booking, Doctors

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_email', 'p_phone', 'doc_name', 'booking_date', 'booked_on')
admin.site.register(Booking, BookingAdmin)
