
import json
import zlib
import base64
import argparse
import shutil
import StringIO

#FIXME: Need custom pyamf... Normal one doesn't support Dictionary (0x11)
import pyamf, pyamf.amf3

class Item(object):
	def __init__(self, id, count):
		self.count = count
		self.id = id

class Block(object):
	def __init__(self, items = [], type = 'Unnamed'):
		self.items = items
		self.type = type
	
class ItemSetObject(object):
	def getString(self):
		return json.dumps(self, cls=ItemSetEncoder)
	def setString(self, string):
		ItemSetDecoder(self).decode(string)
	string = property(getString, setString)

class ItemSet(ItemSetObject):
	def __init__(self, filename = None):
		self.associatedChampions = []
		self.associatedMaps = []
		self.blocks = [Block([], 'Unnamed')]
		self.isGlobalForChampions = True
		self.isGlobalForMaps = True
		self.map = 'any'
		self.mode = 'any'
		self.priority = False
		self.sortrank = 4
		self.title = 'Unnamed'
		self.type = 'global'
		self.uid = ''
		
		if (not (filename is None)):
			with open(filename) as f:
				ItemSetDecoder(self).decode(f.read())

	def getLink(self):
		return base64.b64encode(zlib.compress(self.string, 9))
	def setLink(self, link):
		self.string = zlib.decompress(base64.b64decode(link))
	link = property(getLink, setLink)
	
	def __str__(self):
		return json.dumps(self, cls=ItemSetEncoder, indent=4)

class ItemSets(ItemSetObject):
	def __init__(self, itemSets, timeStamp):
		self.itemSets = itemSets
		self.timeStamp = timeStamp
	def __str__(self):
		return json.dumps(self, cls=ItemSetEncoder, indent=4)
				
class ItemSetEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, object):
			return obj.__dict__
		return super(ItemSetEncoder, self).default(obj)
		
class ItemSetDecoder(json.JSONDecoder):
	def __init__(self, obj = None):
		self.obj = obj			
		super(ItemSetDecoder, self).__init__(object_hook=self.objHook)
		
	def objHook(self, dict):
		if ('itemSets' in dict):
			return ItemSets(dict['itemSets'], dict['timeStamp'])
		elif ('associatedChampions' in dict):
			if self.obj is None:
				self.obj = ItemSet()
			for key, value in dict.iteritems():
				setattr(self.obj, key, value)
			return self.obj
		elif ('items' in dict):
			return Block(dict['items'], dict['type'])
		elif ('id' in dict):
			return Item(dict['id'], dict['count'])
		else:
			raise Exception('Unknown JSON Object...')

class RemoteClass(object):
    def __init__(self, alias):
        self.alias = alias

    def __call__(self, klass):
        pyamf.register_class(klass, self.alias)
        return klass

#FIXME: Why does it have a >???
@RemoteClass(alias='>com.riotgames.platform.gameclient.domain.UserPrefs')
class UserPrefs(object):
	class __amf__:
		amf3 = True
		#FIXME: No clue...
		#static = ('enableAnimationsChanged',)
	
	def __new__(cls, *args, **kwargs):
		obj = object.__new__(cls)
		obj.__init__(*args, **kwargs)
		return obj
	
	def __init__(self, *args, **kwargs):
		#self.enableAnimationsChanged = kwargs.get('enableAnimationsChanged', None)
		self.hadIPTimeBoost = kwargs.get('hadIPTimeBoost', None)
		self.hadXPWinBoost = kwargs.get('hadXPWinBoost', None)
		self.itemSets = kwargs.get('itemSets', None)
		self.selectedPVPOptions = kwargs.get('selectedPVPOptions', None)
		self.b_editor_top_collection_zoom = kwargs.get('b_editor_top_collection_zoom', None)
		self.musicVolumeChanged = kwargs.get('musicVolumeChanged', None)
		self.replayNewbieTip1Shown = kwargs.get('replayNewbieTip1Shown', None)
		self.create_custom_game_mapId = kwargs.get('create_custom_game_mapId', None)
		self.b_game_setup_last_pvp_d = kwargs.get('b_game_setup_last_pvp_d', None)
		self.volumeChanged = kwargs.get('volumeChanged', None)
		self.hadIPWinBoost = kwargs.get('hadIPWinBoost', None)
		self.currentMasteryPage = kwargs.get('currentMasteryPage', None)
		self.hasSeenSocialNetworkPrompt = kwargs.get('hasSeenSocialNetworkPrompt', None)
		self.b_builder_collection_zoom = kwargs.get('b_builder_collection_zoom', None)
		self.chatRoomsTimeStamp = kwargs.get('chatRoomsTimeStamp', None)
		self.b_game_setup_last_practice_d = kwargs.get('b_game_setup_last_practice_d', None)
		self.hadXPTimeBoost = kwargs.get('hadXPTimeBoost', None)
		self.muteChanged = kwargs.get('muteChanged', None)
		self.teamInactivityPendingWarnings = kwargs.get('teamInactivityPendingWarnings', None)
		self.musicMuteChanging = kwargs.get('musicMuteChanging', None)
		self.create_custom_game_spectatorAllowed = kwargs.get('create_custom_game_spectatorAllowed', None)
		self.chatRoomsMaximized = kwargs.get('chatRoomsMaximized', None)
		self.selectedPVEOptions = kwargs.get('selectedPVEOptions', None)
		self.personalImTimeStampsChanged = kwargs.get('personalImTimeStampsChanged', None)
		self.runeStyle = kwargs.get('runeStyle', None)
		self.b_game_setup_last_survival_d = kwargs.get('b_game_setup_last_survival_d', None)
		self.find_custom_game_type_filters = kwargs.get('find_custom_game_type_filters', None)
		self.championSmallIcons = kwargs.get('championSmallIcons', None)
		self.lastStoreRSSRead = kwargs.get('lastStoreRSSRead', None)
		self.prefTimestamps = kwargs.get('prefTimestamps', None)
		self.hasSeenMasteriesReset = kwargs.get('hasSeenMasteriesReset', None)
		self.create_custom_game_serverName = kwargs.get('create_custom_game_serverName', None)
		self.masteryPages = kwargs.get('masteryPages', None)
		self.b_editor_bottom_collection_zoom = kwargs.get('b_editor_bottom_collection_zoom', None)
		self.autoJoinList = kwargs.get('autoJoinList', None)
		self.replayNewbieTip2Shown = kwargs.get('replayNewbieTip2Shown', None)
		self.create_custom_game_pickType = kwargs.get('create_custom_game_pickType', None)
		self.prefDTO = kwargs.get('prefDTO', None)
		self.chatShowMsg = kwargs.get('chatShowMsg', None)
		self.b_editor_double_click_tutorial = kwargs.get('b_editor_double_click_tutorial', None)
		self.create_custom_game_teamSize = kwargs.get('create_custom_game_teamSize', None)
		self.find_custom_game_map_filters = kwargs.get('find_custom_game_map_filters', None)
		self.previousRentals = kwargs.get('previousRentals', None)
		self.lastJoJRSSRead = kwargs.get('lastJoJRSSRead', None)
		self.b_game_setup_last_view = kwargs.get('b_game_setup_last_view', None)
		self.teamInactivityWarnings = kwargs.get('teamInactivityWarnings', None)
		self.find_custom_game_lobbies_filters = kwargs.get('find_custom_game_lobbies_filters', None)
		self.selectedTutorialType = kwargs.get('selectedTutorialType', None)
		self.musicMuteChanged = kwargs.get('musicMuteChanged', None)
	
	def __str__(self):
		return json.dumps(self.__dict__, indent=4)

class PropertiesFile(object):
	def __init__(self, filename, decoder = None, encoder = None, createBackup = True):
		self.filename = filename
		self.data = None		
		self.decoder = decoder
		if self.decoder is None:
			self.decoder = pyamf.amf3.Decoder()
		self.encoder = encoder
		if self.encoder is None:
			self.encoder = pyamf.amf3.Encoder()
		
		self.createBackup = createBackup
			

	def read(self):
		with open(self.filename, 'rb') as f:
			self.decoder.send(f.read())
			self.data = self.decoder.readElement()
	def write(self):
		if self.createBackup:
			shutil.copyfile(self.filename, self.filename + '.bak')

		self.encoder.send(self.data)
		self.encoder.next()
		with open(self.filename, 'wb') as f:
			f.write(self.encoder.stream.getvalue())
		self.encoder.stream.truncate()

if (__name__ == '__main__'):
	parser = argparse.ArgumentParser(description='Installs a itemset into LoL.', prog='LoLISM')
	
	parser.add_argument('-i', '--inject', help='Inject ITEMSET into SUMMONER.', action='store_true')

	print_group = parser.add_mutually_exclusive_group()
	print_group.add_argument('-p', '--print_link', help='Print link of ITEMSET.', action='store_true')
	print_group.add_argument('-j', '--print_json', help='Print json of ITEMSET.', action='store_true')

	parser.add_argument('-s', '--summoner', help='Summoner Properties File')
	parser.add_argument('-m', '--itemset', help='ItemSet in Properties file', type=int)
	
	itemset_group = parser.add_mutually_exclusive_group()
	itemset_group.add_argument('-l', '--link', help='ItemSet link')
	itemset_group.add_argument('-f', '--file', help='ItemSet JSON file')
	
	args = parser.parse_args()
	itemset = ItemSet(args.file)

	if args.link:
		itemset.link = args.link
	
	if args.inject or args.summoner:
		propfile = PropertiesFile(args.summoner or 'Dgby714.properties')
		propfile.read()
		itemSets = ItemSetDecoder().decode(propfile.data.itemSets)
		if args.inject:
			itemSets.itemSets.append(itemset)
			propfile.data.itemSets = itemSets.string
			propfile.write()
		else:
			if args.itemset:
				itemset = itemSets.itemSets[args.itemset]
			else:
				print itemSets
	
	if args.print_link:
		print 'lolism://' + itemset.link

	if args.print_json:
		print itemset
	
