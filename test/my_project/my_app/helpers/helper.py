import jwt
from django.conf import settings
from ..models.tokens import Tokens
def check_token(request):
    header = request.headers.get("Authorization", None)
    if (not header or len(header.split(" ")) != 2 or header.split(" ")[0].lower() != "bearer"):
        return None
    try:
        token = jwt.decode(header.split(" ")[1], settings.SECRET_KEY, algorithms='HS256')
        print(token)
        load_token = Tokens.objects.filter(token = header.split(" ")[1])
        if not load_token:
            print(token)
            return None
        if token["permissions"] == "admin":
            load_token.delete()
            return token
    except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
    return None

def create_token(payload):
    return jwt.encode(payload,settings.SECRET_KEY)