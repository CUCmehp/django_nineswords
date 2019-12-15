__author__ = 'CUCmehp'
__date__ = '2019-1-31 16:23'

from django import template
import logging
from django.urls import reverse

logger = logging.getLogger( 'django' )


class _Menu :
    parents = [ ]
    children = [ ]
    models_icon = { }

    def render( self, context, menus = None ) :
        menus = { } if menus is None else menus
        request = context[ 'request' ]

        ret = ''

        if len( menus ) <= 0 :
            # sorted(self.parents)
            menus = self.parents
            if request.path == reverse( 'admin:index' ) :
                ret = '<li class="active"><a href="%s"><i class="fa fa-dashboard"></i><span>主页</span></a></li>' % (
                    reverse( 'admin:index' ) )
            else :
                ret = '<li><a href="%s"><i class="fa fa-dashboard"></i><span>主页</span></a></li>' % (
                    reverse( 'admin:index' ))

        # for group in menus :
        #     key = [ key for key in group ][ 0 ]
        #     icon = '<i class="fa fa-circle"></i>'
        #
        #     if group[ key ][ 'icon' ] != '' :
        #         if re.match( r'\<([a-z]*)\b[^\>]*\>(.*?)\<\/\1\>', group[ key ][ 'icon' ] ) :
        #             icon = group[ key ][ 'icon' ]
        #         else :
        #             icon = '<i class="%s"></i>' % (group[ key ][ 'icon' ])
        #
        #     if len( group[ key ][ 'children' ] ) > 0 :
        #         r += '<li class="treeview"><a href="#">%s <span>%s</span><span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span></a><ul class="treeview-menu">\n' % (
        #             icon, group[ key ][ 'label' ])
        #
        #         r += self.render( context, group[ key ][ 'children' ] )
        #
        #         r += '</ul></li>\n'
        #
        #     else :
        #         if (request.path == reverse( 'admin:index' )) :
        #             r += '<li><a href="%s">%s <span>%s</span></a></li>\n' % (
        #                 group[ key ][ 'link' ], icon, group[ key ][ 'label' ])
        #         else :
        #             r += '<li><a href="%s">%s <span>%s</span></a></li>\n' % (
        #                 group[ key ][ 'link' ], icon, group[ key ][ 'label' ])

        return ret

    def admin_apps( self, context, reserve ) :
        try:
            request = context[ 'request' ]
            # print( "context[ 'available_apps' ] : " + str( context[ 'available_apps' ] ) )
            # print( "context: " + str( context ) )
            reserve += ''
            for app in context[ 'available_apps' ] :
                reserve += '<li id="app_%s" class="treeview"><a href="#"><i class="fa fa-files-o"></i><span>%s</span><span ' \
                           'class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span></a><ul ' \
                           'class="treeview-menu">' % ( app[ 'app_label' ], app[ 'name' ] )
                for model in app[ 'models' ] :
                    if 'add_url' in model :
                        url = model[ 'add_url' ]

                    if 'change_url' in model :
                        url = model[ 'change_url' ]

                    # if 'delete_url' in model:
                    #     url = model['delete_url']

                    if 'admin_url' in model :
                        url = model[ 'admin_url' ]

                    icon = '<i class="fa fa-circle-o"></i>'
                    # if model['object_name'].title() in self.models_icon:
                    #     if self.models_icon[model['object_name'].title()] != '':
                    #         if re.match(r'\<([a-z]*)\b[^\>]*\>(.*?)\<\/\1\>', self.models_icon[model['object_name'].title()]):
                    #             icon = self.models_icon[model['object_name'].title()]
                    #         else:
                    #             icon = '<i class="%s"></i>' % (self.models_icon[model['object_name'].title()])
                    # 设置选中高亮active状态
                    if request.path == url :
                        reserve += '<li class="active"><a href="%s">%s %s</a></li>' % (url, icon, model[ 'name' ])
                    else :
                        reserve += '<li><a href="%s">%s %s</a></li>' % (url, icon, model[ 'name' ])

                reserve += '</ul></li>'
            logger.debug( 'admin_apps returns: ' + reserve )
        except Exception as exc:
            logger.error( "admin apps get exception: %s", repr( exc ) )
        return reserve


register = template.Library()

Menu = _Menu()


@register.simple_tag( takes_context = True, name = 'menu' )
def menu_tag( context ) :
    # return Menu.admin_apps(context, Menu.render(context))
    # test = """<li>
    #                 <a href="#">
    #                     <i class="fa fa-dashboard"></i> <span>测试</span>
    #                     <span class="pull-right-container">
    #                 <small class="badge pull-right bg-green">new</small>
    #               </span>
    #                 </a>
    #             </li>"""
    return Menu.admin_apps( context, Menu.render( context ) )
