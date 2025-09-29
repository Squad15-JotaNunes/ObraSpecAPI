from django.shortcuts import get_object_or_404
from .models import ReferentialName, Referential

class ReferentialNameServices:
    @staticmethod
    def get(pk):
        return get_object_or_404(ReferentialName, pk=pk)
    @staticmethod
    def list_all():
        return ReferentialName.objects.all()
    @staticmethod
    def delete(pk):
        referential_name = get_object_or_404(ReferentialName, pk=pk)
        referential_name.delete()
        return True

class ReferentialServices:
    @staticmethod
    def get(pk):
        return get_object_or_404(Referential, pk=pk)
    @staticmethod
    def list_all():
        return Referential.objects.all()
    @staticmethod
    def delete(pk):
        referential = get_object_or_404(Referential, pk=pk)
        referential.delete()
        return True