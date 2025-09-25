from django.shortcuts import render
from rest_framework.views import APIView

class ReferentialView(APIView): 

    # Create instance of Referential:
    def post(self, request):
        pass
    
    # Retrieve list of Referentials:
    def get(self, request):
        pass

    # Update instance of Referential:
    def put(self, request, pk):
        pass

    # Delete instance of Referential:
    def delete(self, request, pk):
        pass

