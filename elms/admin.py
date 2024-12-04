from django.contrib import admin

# Register your models here.

from .models import CustomUser, LeaveApplication, LeaveBalance, Department

# Register the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'surname', 'email', 'phone_number')
    search_fields = (
        'first_name', 'surname', 'email')
    llist_filter = ('gender', 'department')

# Register the LeaveApplication model
@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'leave_type', 'start_date', 'end_date', 'status', 'applied_on', 'updated_on')
    list_filter = ('leave_type', 'status', 'applied_on')
    search_fields = ( 'user__first_name', 'user__surname')
    date_hierarchy = 'applied_on'
    ordering = ('-applied_on',)

# Register the LeaveBalance model
@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_days', 'used_days', 'remaining_days')
    search_fields = ( 'user__first_name', 'user__surname')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_abbreviation', 'department_code', 'creation_date', 'modified_date')
    search_fields = ('department_name', 'department_abbreviation', 'department_code')
    list_filter = ('creation_date',)
    ordering = ('-creation_date',)