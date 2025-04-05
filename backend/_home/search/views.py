from rest_framework import generics
from rest_framework.response import Response
from . import client

class SearchListView(generics.GenericAPIView):
    """
    View for performing searches and returning results.
    """
    def get(self, request, *args, **kwargs):
        # Extract parameters from the request
        query = request.GET.get('q')
        if not query:
            return Response({'error': 'Search query is required'}, status=400)

        # Check user authentication
        user = None
        if request.user.is_authenticated:
            user = request.user.username

        # Get other query parameters like 'public' and 'tag'
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None

        # Perform the search using the client
        results = client.perform_search(query, tags=tag, user=user, public=public)

        return Response(results)
