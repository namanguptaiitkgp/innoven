from django.contrib import admin

# Register your models here.
from projects.models import Project, DealStage, VDcomp, Director, DSdate, Member, Stage, Source, Sector, Engagement, Partner, Investor, Location, pDesignation, Dialouge, Doc, OStatus

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Stage)
admin.site.register(Source)
admin.site.register(DealStage)
admin.site.register(Sector)
admin.site.register(Engagement)
admin.site.register(Partner)
admin.site.register(Investor)
admin.site.register(Location)
admin.site.register(pDesignation)
admin.site.register(Dialouge)
admin.site.register(Doc)
admin.site.register(OStatus)
admin.site.register(VDcomp)
admin.site.register(Director)
admin.site.register(DSdate)

