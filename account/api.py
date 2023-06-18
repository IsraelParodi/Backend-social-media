from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import SignupForm


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "email": request.user.email,
            "isActive": request.user.is_active,
            "isStaff": request.user.is_staff,
            "isSuperuser": request.user.is_superuser,
        }
    )


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    form = SignupForm(data)
    if form.is_valid():
        try:
            form.save()
            # TODO: Send verification email later
            return JsonResponse({"status": "success"}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)
