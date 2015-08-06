from collections import namedtuple
from threading import Lock


TIMEFMT = '%Y%m%d_%H%M%S'

lock = Lock()


# user/automata



class DB:
	def __init__(self, path):
		self._fh = None
		self.db = defaultdict(dict)
		for line in open(path):
			...
		self._fh = open(path, 'a')

	def add(self, data):
		with lock:
			db = self.db['%s/%s' % (data.user, data.automata)]
			if data.timestamp in db:
				new = False
				changed = db[data.timestamp] == data
			else:
				new = True
			db[data.timestamp] = data
			if new or changed:
				self.log(data)
			return 'new' if new else 'updated' if changed else 'unchanged'

	def log(self, data):
		if self._fh:
			self._fh.write(...serialise(data)...)

	def latest(self, key):
		db = self.db[key]
		return db[max(db)]


def auth(user, passphrase):
	return authdict.get(user) == passphrase


def latest(key):
	# key = user/automata
	data = db.latest(key)
	return data



def add(data):
	# data = {user:string, automata:string, timestamp:string, deplist:list, joblist:JobList,}
	data = request.json or {}
	if auth(data.get('user'), request.query.get('passphrase')):
		result = db.add(data)
		return result
	else:
		return HTTPError(403)



#(setq indent-tabs-mode t)

def readauth(filename):
	d = {}
	with open(filename) as fh:
		for line in fh:
			if line.startswith('#'):  continue
			line = line.rstrip('\n').split(':')
			if line and len(line) == 2:
				d[line[0]] = line[1]
	return d



if __name__ == "__main__":
	path = argv..
	authfile = argv..
	db = DB(path)
	pass
