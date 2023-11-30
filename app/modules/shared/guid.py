import uuid


class Guid():
	def new():
		return str(uuid.uuid4())
