import spacy

class Template:
	def __init__(self):
		self.data = {
			'tenant_notice': 'condition left return obligations provide timeframe via property payment rent portion returned accordance deposit keys tenancy advice tenant fulfilled method lease outstanding send vacated withhold requires described relation particular requested',
			'resignation': 'feel per consequently growth work departure company end resignation grateful tender day working relieving prior free intend discuss addressed pursuing calculate issue need employment contact last support accept matters thank provided continue encouragement opportunities acceptance incredibly position',
			'breach_of_contract': 'rectify required take agreement contract clause breached come specific limiting breach fail dated specifically attention section future appropriate entered seek confirm available legal terms commit manner documents acknowledge refer forced action please hereinafter',
			'defamation': 'cause distress remove made carrying laws apology serves defamatory may actions cease unwanted period content information hereby within writing retraction damage refrain applicable activities limitation personal defamation apologise demand reputation receipt statements notify following making inter-alia attached emotional knowledge thereby substantial intention remedies letter including above-mentioned defame trying harassing kinds spreading harm caused professional damages limited reference examples prejudice request rights unconditionally baseless false character several accusations publish highly sent notice days also us suffer since completed without immediately desist annoying allegations',
			'rti': 'india requisite charges deposited inform favoring received sovereignty act rti citizen information detrimental 2005 poverty right to banker circumstances linedraft case share seek bpl interest'
		}
		self.nlp = spacy.load('en_core_web_md')

	def get_category(self, query):
		pages = {
			'tenant_notice': 'Tenancy Ending Notice',
			'resignation': 'Resignation Letter',
			'breach_of_contract': 'Breach of Contract (or a clause)',
			'defamation': 'Cease and Desist (Defamation)',
			'rti': 'Right To Information'
		}
		result = 0
		category = None
		query = self.nlp(query.lower())
		for cat in self.data:
			curr = query.similarity(self.nlp(self.data[cat]))
			if curr > result:
				result = curr
				category = cat
		return (category, pages[category]) if category else (category, 'No results found!')
