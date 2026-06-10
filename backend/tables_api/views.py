""" Module that handles the C.R.U.D. operations for the tables db."""

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tables import NextcloudTablesClient

@api_view(["GET"])
def view_rows(request, view_id: int):
    client = NextcloudTablesClient()
    rows = client.get_view_rows(view_id)
    return Response(rows)
