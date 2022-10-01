import requests
import urllib

from torrent_record import TorrentRecord

BASE_QUERY = "{}q.php?q={}"


class TorrentQuery:
	def __init__(self, api_location="http://apibay.org/"):
		self.api_location = api_location

	def query(self, query_string, max_results=5):
		return self._pick_results(self._query_api(self._get_query_url(query_string)), max_results)

	def _get_query_url(self, query_string):
		return BASE_QUERY.format(self.api_location, urllib.parse.quote_plus(query_string))

	def _query_api(self, query):
		return requests.get(query).json()

	def _pick_results(self, all_results, max_results):
		all_results.sort(key=lambda k: int(k.get('seeders')), reverse=True)
		return [TorrentRecord.from_dict(i) \
				for i in all_results[:max_results]]
