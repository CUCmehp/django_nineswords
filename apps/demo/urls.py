__author__ = 'CUCmehp'
__date__ = '2019-5-9 14:50'

from django.urls import path
from demo.views import PaginationDemo

app_name = 'demo'

urlpatterns = [
    # 分页Demo
    path( 'pagination_demo/', PaginationDemo.as_view(), name = 'pagination_demo', ),
]
