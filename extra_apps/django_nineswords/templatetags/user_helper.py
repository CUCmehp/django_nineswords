from django.utils.html import format_html
from django.utils.safestring import mark_safe

__author__ = 'CUCmehp'
__date__ = '2019-3-8 15:42'

import django
from django import template
from django.conf import settings
import logging
from django.contrib.admin.views.main import PAGE_VAR

logger = logging.getLogger( 'django' )

DOT = '.'


def is_authenticated( user ) :
    if django.VERSION >= (2, 0) :
        return user.is_authenticated
    else :
        return user.is_authenticated()


register = template.Library()


@register.simple_tag()
def logout_url() :
    str_url = getattr( settings, 'LOGOUT_URL', '/admin/logout/' )
    logger.info( 'logout_url get url: ' )
    return str_url


# @register.simple_tag(takes_context=True)
# def avatar_url(context, size=None, user=None):
#     # TODO: Make behaviour configurable
#     user = context['request'].user if user is None else user
#     return 'https://www.gravatar.com/avatar/{hash}?s={size}&d=mm'.format(
#         hash=md5(user.email.encode('utf-8')).hexdigest() if is_authenticated(user) else '',
#         size=size or '',
#     )

@register.simple_tag
def pami_paginator_number( cl, i ) :
    """
    Generate an individual page index link in a paginated list.
    """
    if i == DOT :
        # return '... '
        return format_html('<li class="disabled"><a>...</a></li>')
    elif i == cl.page_num :
        return format_html( '<li class="active"><a href="#">{}</a></li>',
                            i + 1 )  # return format_html('<span class="this-page">{}</span> ', i + 1)
    else :
        return format_html( '<li><a href="{}"{}>{}</a></li> ', cl.get_query_string( { PAGE_VAR : i } ),
                            mark_safe( ' class="end"' if i == cl.paginator.num_pages - 1 else '' ), i + 1 )


@register.simple_tag
def pami_result_count( cl ) :
    if cl.result_count == 1 :
        str_model_name = cl.opts.verbose_name
    else :
        str_model_name = cl.opts.verbose_name_plural
    return format_html( '<p>共{}条{}</p>', cl.result_count, str_model_name )


@register.simple_tag
def pami_paginator_previous( cl ) :
    if cl.page_num == 0 :
        return format_html( '<li class="disabled"><a href="#">上一页</a></li>' )
    else :
        return format_html( '<li><a href="{}">上一页</a></li> ', cl.get_query_string( { PAGE_VAR : cl.page_num - 1 } ) )


@register.simple_tag
def pami_paginator_next( cl ) :
    if cl.page_num == cl.paginator.num_pages - 1 :
        return format_html( '<li class="disabled"><a href="#">下一页</a></li>' )
    else :
        return format_html( '<li><a href="{}">下一页</a></li> ', cl.get_query_string( { PAGE_VAR : cl.page_num + 1 } ) )


@register.simple_tag()
def get_sys_common_title():
    str_sys_common_title = getattr( django.conf.settings, "SYS_COMMON_TITLE", "nineswords管理后台" )
    return format_html( str_sys_common_title )


# 获取支撑公司
@register.simple_tag( name = 'get_tech_company' )
def get_tech_company() :
    return getattr( django.conf.settings, "TECH_COMPANY", "技术支撑公司" )


# 获取支撑公司链接
@register.simple_tag( name = 'get_tech_company_href' )
def get_tech_company_href() :
    return getattr( django.conf.settings, "TECH_COMPANY_HREF", "技术支撑公司" )
