
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def home_api(request):
    data = {
        "status": "success",
        "message": "Welcome to My Django REST API!",
        "developer": "Ratul Hasan",
        "version": "1.0",
    }

    return Response(data)
