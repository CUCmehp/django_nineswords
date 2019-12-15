import logging

from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from demo.models import Country

# Create your views here.
from django_nineswords.paginator import Paginator, PageNotAnInteger


logger = logging.getLogger( 'django' )


class PaginationDemo( View ):
    def get( self, request ):
        try :
            _country_list = Country.objects.all()
            try :
                page = self.request.GET.get( 'page', 1 )
            except PageNotAnInteger :
                page = 1  # 这里指从all中取10个出来，每页显示10个
            p = Paginator( _country_list, 10, request = request )
            country_list = p.page( page )
            return render( request, 'admin/pagination_demo.html', { 'country_list' : country_list } )
        except Exception as exc :
            logger.error( "PaginationDemo get exception, %s", repr( exc ) )
            return render_to_response( "500.html" )
