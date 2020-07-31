from datetime import datetime, timedelta

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def list_languages(request):
    """
    Dict of languages used in top 100 trending repositories on Github(GH),
    with following attributes:
    + the number of repos using the language
    + list of repos' urls (api + html urls)
    """
    today = datetime.now()

    url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(
        today)
    response = requests.get(url)

    return Response(response)
