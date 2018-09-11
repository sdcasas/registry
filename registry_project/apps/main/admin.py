from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


# from .forms import DepositForm, WithdrawForm

from . import models
from .forms import CourseForm


class PaymentInline(admin.StackedInline):
    '''
    Tabular Inline View for Payment
    '''
    model = models.Payment
    # min_num = 3
    # max_num = 20
    extra = 1
    # raw_id_fields = (,)
    fieldsets = [
        (None, {
            'fields': [('receipt', 'value'),  ('date_pay', 'period'), 'concept']
        }),
    ]


class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('__str__', 'email', 'dni', 'username_discord', '_get_teen')
    # list_filter = ('',)
    search_fields = ('first_name','last_name', 'email', 'dni', 'username_discord')
    inlines = (PaymentInline,)

    fieldsets = [
        (None, {
            # 'classes': ('suit-tab suit-tab-basico',),
            'fields': [('last_name', 'first_name'), ('dni', 'sex'), 'email', 
            ('cellphone', 'username_discord')]
        }),
    ]


    def _get_teen(self, obj):
        if obj.teen.all().count():
            return [t.name for t in obj.teen.all()]
        return None

    _get_teen.show_description = 'Equipo'

    # def has_add_permission(self, request):
    #     return False

    # def has_change_permission(self, request, obj=None):
        
    #     if not request.user.is_superuser:
    #         return True
    #     else:
    #         return False

    # def process_deposit(self, request, account_id, *args, **kwargs):
    #     return self.process_action(
    #         request=request,
    #         account_id=account_id,
    #         action_form=DepositForm,
    #         action_title='Deposit',
    #     )
    # def process_withdraw(self, request, account_id, *args, **kwargs):
    #     return self.process_action(
    #         request=request,
    #         account_id=account_id,
    #         action_form=WithdrawForm,
    #         action_title='Withdraw',
    #     )
     
    # def process_action(
    #     self,
    #     request,
    #     account_id,
    #     action_form,
    #     action_title
    #     ):
    #     account = self.get_object(request, account_id)
    #     if request.method != 'POST':
    #         form = action_form()
    #     else:
    #         form = action_form(request.POST)
    #         if form.is_valid():
    #             try:
    #                 form.save(account, request.user)
    #             except errors.Error as e:
    #                 # If save() raised, the form will a have a non
    #                 # field error containing an informative message.
    #                 pass
    #             else:
    #                 self.message_user(request, 'Success')
    #                 url = reverse(
    #                     'admin:account_account_change',
    #                    args=[account.pk],
    #                     current_app=self.admin_site.name,
    #                 )
    #                 return HttpResponseRedirect(url)
    #     context = self.admin_site.each_context(request)
    #     context['opts'] = self.model._meta
    #     context['form'] = form
    #     context['account'] = account
    #     context['title'] = action_title
    #     return TemplateResponse(
    #         request,
    #         'admin/account/account_action.html',
    #         context,
    #     )




admin.site.register(models.Student, StudentAdmin)

admin.site.register(models.Module)
admin.site.register(models.Mentor)
# admin.site.register(models.Student)
admin.site.register(models.Teen)
# admin.site.register(models.Course)
admin.site.register(models.Payment)


class CourseAdmin(admin.ModelAdmin):
    '''
        Admin View for Course
    '''
    form = CourseForm
    # list_display = ('name',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)

admin.site.register(models.Course, CourseAdmin)