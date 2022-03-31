from django.contrib import admin
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'weight', 'measure', 'description', 'picture']


# Register your models here.
from .models import Autorisation
admin.site.register(Autorisation)

from .models import Comments
admin.site.register(Comments)
#
from .models import Restarant
admin.site.register(Restarant)

from .models import Position
admin.site.register(Position)


from .models import Personal
admin.site.register(Personal)

from .models import Menu
admin.site.register(Menu,MenuAdmin)

from .models import Measure
admin.site.register(Measure)


from .models import Store
admin.site.register(Store)

from .models import Booking
admin.site.register(Booking)