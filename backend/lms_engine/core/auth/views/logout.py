from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.models import AccessToken, RefreshToken
from rest_framework.decorators import api_view


@api_view(["POST"])
def logout(request):
    """
    Revoke the user's access token.
    """
    token = request.data.get("token")

    if not token:
        return Response(
            {"error": "Token is required."}, status=status.HTTP_400_BAD_REQUEST
        )
    
    if token != AccessToken.objects.get(user=request.user).token:
        return Response(
            {"error": "Token does not belong to the authenticated user."}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        access_token = AccessToken.objects.get(token=token)
        RefreshToken.objects.filter(access_token=access_token).delete()
        access_token.delete()
        return Response(
            {"message": "Logged out successfully."}, status=status.HTTP_200_OK
        )
    except AccessToken.DoesNotExist:
        return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
