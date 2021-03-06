#from django.contrib import admin
## Import your models here.
#from defects.models import *
#
#class NewAppModelAdmin(admin.ModelAdmin):
#    list_display = ('last_name', 'first_name', 'user', 'submitted', 'tx_success')
#    save_on_top = True
#    
#    actions = ['archive']
#    
#    def archive(self, request, queryset):
#        rows_updated = queryset.update(is_archived=True)
#        if rows_updated == 1:
#            message_bit = "1 applicant was"
#        else:
#            message_bit = "%s applicants were" % rows_updated
#
#        self.message_user(request, "%s successfully archived." % message_bit)
#        
#
##admin.site.register(Model, NewAppModelAdmin)
#admin.site.register(Defect)
from django.contrib import admin
from forum.models import *

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Reply)