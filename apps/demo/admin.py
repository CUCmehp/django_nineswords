from django.contrib import admin
from demo.models import Continent, Country, City


# Register your models here.


@admin.register( Continent )
class ContinentAdmin( admin.ModelAdmin ) :
    list_display = ('name', 'order',)


@admin.register( Country )
class CountryAdmin( admin.ModelAdmin ) :
    # list_display = ('name',)
    search_fields = ('name', 'code',)
    # list_display = ('name', 'code', 'link_to_continent', 'independence_day', )
    list_display = ('name', 'code', 'independence_day',)
    list_filter = ('continent', 'independence_day', 'code',)
    suit_list_filter_horizontal = ('code', 'population')
    list_select_related = True
    # inlines = (CityInline,)
    # date_hierarchy = 'independence_day'
    list_per_page = 10

    fieldsets = [
        ( None, { 'fields' : [ 'name', 'code', 'continent', 'independence_day' ] }),
        ( 'Statistics', {
          'classes' : ('suit-tab suit-tab-general',), 'description' : 'EnclosedInput widget examples',
          'fields' : [ 'area', 'population' ] }),
        ( 'Autosized textarea', {
            'classes' : ('suit-tab suit-tab-general',),
            'description' : 'AutosizedTextarea widget example - adapts height '
            'based on user input',
            'fields' : [ 'description' ] }),
        ( 'Architecture', {
            'classes' : ('suit-tab suit-tab-cities',),
            'description' : 'Tabs can contain any fieldsets and inlines',
            'fields' : [ 'architecture' ] }), ]


@admin.register( City )
class CityAdmin( admin.ModelAdmin ) :
    list_display = ('name', 'country', 'is_capital', 'area', 'population',)
    search_fields = ('name',)
    list_filter = ('is_capital',)
