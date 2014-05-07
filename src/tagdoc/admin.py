from django.contrib import admin
from tagdoc.models import TagGroup, Tag, ServerType, Server, Service, ServerTag, ServiceServer

admin.site.register(TagGroup)
admin.site.register(Tag)
admin.site.register(ServerType)
admin.site.register(Server)
admin.site.register(Service)
admin.site.register(ServerTag)
admin.site.register(ServiceServer)
