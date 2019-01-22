from django.contrib import admin

# Register your models here.
from material.models import rawMaterials, HeavySetalSlag, RedMud, SteelSlag, VantaiSlag, NiIronSlag

admin.site.register(rawMaterials)
admin.site.register(HeavySetalSlag)
admin.site.register(RedMud)
admin.site.register(SteelSlag)
admin.site.register(VantaiSlag)
admin.site.register(NiIronSlag)

