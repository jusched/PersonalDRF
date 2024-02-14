from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    # Override auth header keyword
    keyword = "Bearer"
    # Can be deleted on admin view
