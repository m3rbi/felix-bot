from torrent_record import TorrentRecord


class TorrentState:
	def __init__(self, torrent_record, progress):
		self.record = torrent_record
		self.progress = f"{round(progress * 100, 2)}%"

	def __str__(self):
		return f"[{self.progress}] {str(self.record)}"

	@staticmethod
	def from_dict(data):
		return TorrentState(TorrentRecord.from_dict(data), data.get('progress'))
