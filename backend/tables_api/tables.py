''' This module contains the communication logic with the modules database, via
    the tables (nextcloud) api.

    It's used for retrieving the latest module specific information.
'''

import os
import traceback
import requests
from requests.auth import HTTPBasicAuth

REQUEST_TIMEOUT = 30

try:
    tablesURL = os.environ['TABLES_URL']
    tablesUsername = os.environ['TABLES_USERNAME']
    tablesPassword = os.environ['TABLES_PASSWORD']
except KeyError as exc:
    raise KeyError(traceback.format_exc()) from exc


class NextcloudTablesClient:
    def __init__(self):
        self.base_url = tablesURL  # endet mit /
        self.auth = HTTPBasicAuth(
            tablesUsername,
            tablesPassword,
        )

    def _get(self, path: str):
        response = requests.get(
            f'{self.base_url}{path}',
            auth=self.auth,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def get_columns(self, view_id: int) -> dict[int, str]:
        data = self._get(f'api/1/views/{view_id}/columns')
        return {col['id']: col['title'] for col in data}

    def get_view_rows(self, view_id: int) -> list[dict]:
        columns = self.get_columns(view_id)
        rows = self._get(f'api/1/views/{view_id}/rows')
        result = []
        for row in rows:
            result.append({
                columns[cell['columnId']]: cell['value']
                for cell in row['data']
            })
        return result


def main() -> None:
    ''' main method'''
    view_id = int(os.environ.get('TABLE_VIEW_ID', '3708'))
    client = NextcloudTablesClient()

    print(f'Fetching view {view_id} from Nextcloud Tables...')
    columns = client.get_columns(view_id)
    rows = client.get_view_rows(view_id)

    print(f'Columns ({len(columns)}):')
    for column_id, title in columns.items():
        print(f'  {column_id}: {title}')

    print(f'Rows ({len(rows)}):')
    for row in rows[:5]:
        print(row)


if __name__ == '__main__':
    main()
