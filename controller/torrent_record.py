
class TorrentRecord:
	def __init__(self, name, size, info_hash):
		self.name = name
		self.size = float(size)
		self.info_hash = info_hash

	def __str__(self):
		return f"[{bytesize_format(self.size)}] {self.name}"

	def get_magnet(self):
		return f"magnet:?xt=urn:btih:{self.info_hash}"

	@staticmethod
	def from_dict(data):
		return TorrentRecord(data.get('name'),
							 data.get('size'),
							 data.get('info_hash'))



def bytesize_format(num):
	for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
		if abs(num) < 1024.0:
			return f"{num:3.1f}{unit}B"
		num /= 1024.0
	return f"{num:.1f}YiB"
