from qbittorrent import Client
from torrent_state import TorrentState


class TorrentController:
	def __init__(self, client_address, username='admin', password='adminadmin'):
		self.client = Client(client_address)
		self.client.login(username, password)
		self.client.set_preferences(max_ratio_enabled=True, max_ratio=0)

	def download_magnet(self, magnet_link):
		self.client.download_from_link(magnet_link)

	def delete_info_hash(self, info_hash):
		self.client.delete_permanently(info_hash)

	def list_all_torrents(self):
		return self._get_torrents_by_filter(lambda _: True)

	def list_downloading_torrents(self):
		return self._get_torrents_by_filter(lambda k: k.get('state') == 'downloading')

	def list_finished_torrents(self):
		return self._get_torrents_by_filter(lambda k: k.get('progress') == 1)

	def _get_torrents_by_filter(self, filter_cond):
		return [TorrentState.from_dict(i) \
				for i in self.client.torrents() if filter_cond(i)]
