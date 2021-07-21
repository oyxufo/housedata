from django.contrib import admin
from django.urls import path
import showdata.views

urlpatterns = [

    # path('add/',showdata.views.add_orm),
    # path('delete/',showdata.views.delete_orm),
    # path('change/',showdata.views.change_orm),
    # path('query/',showdata.views.query_orm),
    path('all/',showdata.views.all_page),
    path('delete/',showdata.views.delete_student),
    path('change/',showdata.views.change_page),
    path('updatestudent/',showdata.views.update_student),
    path('add/',showdata.views.addstu),


    path('test3/',showdata.views.test3),
    path('to_add/',showdata.views.to_add),
    path('to_edit/',showdata.views.to_edit),
    path('editdata/',showdata.views.editdata),
    path('test22/',showdata.views.test22),
    path('deletedata/',showdata.views.deletedata),
    path('adddata/',showdata.views.adddata),
    path('delete_one_data/',showdata.views.delete_one_data),


]