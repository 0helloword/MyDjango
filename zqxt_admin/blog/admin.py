from django.contrib import admin
from .models import Article,Person

# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','pub_date','update_time','status',)#查询列表增加列展示
    search_fields=('title','content',)#查询条件增加搜索功能
    def save_model(self,request,obj,form,change):
        if change:#更改的时候
            obj_original=self.model.objects.get(pk=obj.pk)
        else:#新增的时候
            obj_original=None
        obj.user=request.user
        obj.save()
    def delete_model(self,request,obj):
        obj.delete()
#     list_filter('status',)
admin.site.register(Article,ArticleAdmin)


class MyModelAdmin(admin.ModelAdmin):#未验证！如果是超级管理员就列出所有的，如果不是，就仅列出访问者自己相关的
    def get_queryset(self, request):
        qs=super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

class PersonAdmin(admin.ModelAdmin):
    list_display=('full_name',)
    search_fields=('first_name',)
    def get_search_results(self, request, queryset, search_term):#定制搜索功能?
        queryset,use_distinct=super(PersonAdmin,self).get_search_results(request,queryset,search_term)
        try:
            search_term_as_int=int(search_term)
            queryset |=self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return  queryset,use_distinct
admin.site.register(Person,PersonAdmin)








