from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField


### taggroups - defined by user
class TagGroup(models.Model):
    name = models.CharField(max_length=100)


### tags - data comes from from user or scripts
class Tag(models.Model):
    group = models.ForeignKey(TagGroup)
    name = models.CharField(max_length=100)


### the servertypes - defined by user
class ServerType(models.Model):
    name = models.CharField(max_length=100)
    vmhost = models.BooleanField()


### servers - defined by user
class Server(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    hostname = models.CharField(max_length=100)
    type = models.ForeignKey(ServerType)
    selfmanaged = models.BooleanField()
    tags = models.ManyToManyField(Tag, through='ServiceTag')


### the services - defined by user
class Service(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)


### the relation between servers and their tags
class ServerTag(models.Model):
    server = models.ForeignKey(Server)
    tag = models.ForeignKey(Tag)
    data = models.CharField(max_length=1000)


### the relation between services and servers
class ServiceServer(models.Model):
    service = models.ForeignKey(Service)
    server = models.ForeignKey(Server)
    
