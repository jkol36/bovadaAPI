import requests
import json
from betstream.bovadaAPI.bovadaAPI.search_dictionary_for_certain_keys import search_dictionary_for_certain_keys



class PlaceBet(object):

	def _bovada_payload_blueprint(self):
		return json.loads('{"channel":"WEB_BS","selections":{"selection":[{"outcomeId":"93276304","id":0,"system":"A","priceId":"80267125","oddsFormat":"DECIMAL"}]},"groups":{"group":[{"type":"STRAIGHT","groupSelections":[{"groupSelection":[{"selectionId":0,"order":0}]}],"id":0}]},"bets":{"bet":[{"betType":"SINGLE","betGroups":{"groupId":[0]},"stakePerLine":50,"isBox":false,"oddsFormat":"DECIMAL","specifyingRisk":true}]},"device":"DESKTOP"}')

	def replace_priceId(self, new_price_id, d):
		cloned_d= d
		cloned_d["selections"]["selection"][0]["priceId"] = new_price_id
		return cloned_d
		

	def replace_outcomeId(self, new_outcome_id, d):
		cloned_d= d
		cloned_d["selections"]["selection"][0]["outcomeId"] = new_outcome_id
		return cloned_d

	def replace_stake(self, new_stake, d):
		cloned_d = d
		cloned_d["bets"]["bet"][0]["stakePerLine"] = new_stake
		return cloned_d

	def build_bet_selection(self, outcome_id, price_id, stake):
		origdict = self._bovada_payload_blueprint()
		updated_outcome_id = self.replace_outcomeId(outcomeId, origdict)
		updated_stake = self.replace_stake(stake, origdict)
		updated_price_id = self.replace_priceId(priceId, origdict)
		return origdict
	
	def bet_went_through(json):
		print json
	def place(self, data, cookies, headers):
		if cookies and headers and data:
			response = requests.post('https://sports.bovada.lv/services/sports/bet/betslip', headers=headers, cookies=cookies, data=data)
			if response.status_code == 200:
				status = search_dictionary_for_certain_keys("response", response.json())
				if status:
					print "got status"
					key = search_dictionary_for_certain_keys("key", status)
					if key:
						print "got the key"
						r = requests.get("https://sports.bovada.lv/services/sports/bet/betslip/{}".format(key))
						if bet_went_through(r.json()):
							return True
						else:
							return False

				try:
					print response.keys()
					print response.json()
				except Exception, e:
					print e
				return True
			else:
				print response.reason
				print response.status_code
		else:
			raise Exception("can't place bet without cookies or headers")





