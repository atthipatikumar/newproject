from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from sampledata.models import Onlineregister, Login

class FirstpageResource(ModelResource):
    class Meta:
        collection_name = "onlineregister"
        queryset = Onlineregister.objects.all()
        resource_name = 'register1'
        authorization = Authorization()


class SecondpageResource(ModelResource):
    class Meta:
        collection_name = "login"
        queryset = Login.objects.all()
        resource_name = 'login1'
        authorization = Authorization()

