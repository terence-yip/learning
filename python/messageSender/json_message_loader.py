import json

class json_message_loader:
	def load_messages(self, messages_path):
		file_contents = self.read_file(messages_path)
		if(file_contents):
			return self.decode_json(file_contents)

	def read_file(self, messages_path):
		try:
			fh = open(messages_path, "r")
			file_contents = str.join('\n', fh.readlines())
			fh.close()
			return file_contents
		except:
			print("Failed to open file: " + messages_path)
			return None

	def decode_json(self, file_contents):
		json_object = json.loads(file_contents)
		return json_object

