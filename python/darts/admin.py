
from django.contrib.admin import site, ModelAdmin
from models import Player
 
class PlayerAdmin(ModelAdmin):
    list_display = ('name', 'email', 'estimate', 'result', 'score')

site.register(Player, PlayerAdmin)

