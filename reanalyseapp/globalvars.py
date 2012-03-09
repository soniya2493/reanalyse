# -*- coding: utf-8 -*-
############################################################

# in edBrowse / esBrowse (height is set in css
LITTLEFRISEMAXWIDTH = 100

# see settings.py
LANG_CHOICES = (
	('FR', 'Français'),
	('EN', 'English'),
)

# internal status for models
STATUS_CHOICES = (
	('0', 'OK'),
	('-1', 'Failed'),		# problem
	('5', 'Waiting'),		# tei waiting to be processed
	('1', 'Loading'),	
	('2','Parsing'),		# tei processed
	('3','Styling'),		# deprecated ?
	('4','**Internal use'),
	('77', '**You won something')
)

############################################################ DOCUMENTS meta_documents.csv
# A) meta_documents.csv : COLUMN *category1 that are accepted, and their translation in the view
# QUALI "RESEARCH PHASE"
DOC_CAT_1={}
DOC_CAT_1['preparatory']	= 'Preparatory'
DOC_CAT_1['terrain'] 		= 'Fieldwork'
DOC_CAT_1['data'] 			= 'Data'
DOC_CAT_1['result'] 		= 'Result'
DOC_CAT_1['enrich'] 		= 'Complement'
DOC_CAT_1['misc'] 			= 'Misc'
DOC_CAT_1['verbatim'] 		= '?Verbatim?'	

# B) meta_documents.csv : COLUMN *category2 that are accepted, and their translation in the view
# QUALI "DOCUMENT TYPE"
DOC_CAT_2={}
DOC_CAT_2['transcr'] 	= 'Transcr'
DOC_CAT_2['pv'] 		= 'Minutes'
DOC_CAT_2['note'] 		= 'Notes'
DOC_CAT_2['video'] 		= 'Video'
DOC_CAT_2['audio'] 		= 'Audio'
DOC_CAT_2['resum'] 		= 'Summary'
DOC_CAT_2['analyse'] 	= 'Analysis'
DOC_CAT_2['quest'] 		= 'Quest'
DOC_CAT_2['publi'] 		= 'Publ'
DOC_CAT_2['com'] 		= 'Com'
DOC_CAT_2['rap'] 		= 'Rep'
DOC_CAT_2['recrut'] 	= 'Recr'
DOC_CAT_2['guide'] 		= 'Guide'
DOC_CAT_2['misc'] 		= 'Misc'

# C) meta_documents.csv : COLUMN *mimetype . 
DOCUMENT_MIMETYPES 	=  ['ese','tei']			# special files (parsed)
DOCUMENT_MIMETYPES	+= ['pdf','htm','csv']		# normaly displayed docs
DOCUMENT_MIMETYPES 	+= ['link','ref']			# doc without local file


# documents are parsed only if they are in A) & B) & C)
# note that ese is also processed, but in a different way. see importexport.py

# types of document from the django models point of view
DOCUMENT_TYPE_CHOICES = (
	('TEI', 'XML TEI'),
	('PDF', 'PDF'),
	('HTM', 'HTML File'),
	('CSV', 'CSV Table'),
	('LINK', 'External link'),
	('REF', 'Only reference'),
	#('TXT', 'Text File'),
	#('RTF', 'RTF'),			# rather use htm for the moment, it's simpler
	#('ATL', 'XML Atlas.Ti'),	# ...forget about it for the moment (data too much unstructured)
	#('CTX', 'CAQDAS RTF'),		# ...forget about it for the moment (data too much unstructured)
)

############################################################ SPEAKERS meta_speakers.csv
# Speaker type translator from meta_speakers.csv
SPEAKER_TYPE_CSV_DICT = {
	'investigator'	:'INV',		# (esBrowse off) researcher / interviewer
	'speaker'		:'SPK',		# (public) main spk(s) interviewed
	'protagonist'	:'PRO',		# (public) not interviewed
	'figurant'		:'FIG',		# (esBrowse off) just mentionned
}
# only public (ie listed on esBrowse) speakers are considered for viz: attributes, ngrams, etc...

# Speaker types for django model
SPEAKER_TYPE_CHOICES = (
	('INV', 'Investigator'),
	('SPK', 'Speaker'),
	('PRO', 'Protagonist'),
	('FIG', 'Figurant'),
	('OTH', 'Unknown'),
)

# COLORS for TYPES
SPK_COLORS={}
SPK_COLORS['INV']='#EFEDFC'
SPK_COLORS['SPK']='#E3FBE9'
SPK_COLORS['PRO']='#FFDC98'
SPK_COLORS['FIG']='#FFDC98'
SPK_COLORS['OTH']='#FFFFFF'

# To know if we show/hide spk attributesin the view - based on .startswith("_")
ATTRIBUTE_PUBLICY_CHOICES = (
	('0', 'Private'),
	('1', 'Public'),
	('2', '**Unused'),
	('7', 'for Spok'),
)

################################################################################ VERBATIM
########## PONCTUATION
SENTENCE_UTT_SYMBOLS = {}
SENTENCE_UTT_SYMBOLS['exclamative']='! '
SENTENCE_UTT_SYMBOLS['declarative']='. '
SENTENCE_UTT_SYMBOLS['interrogative']='? '
SENTENCE_UTT_SYMBOLS['not_classified']=' ' # and other keys



########## CODES ACTIVATED (every code need to be declared in CODES DEFINITIONS TOO ! see below )
# ACTIVATED CODES = those in TextStreamTimeline viz (in order) - nb: if there is not code in texte, it will not show on viz !
STREAMVIZCODES={}
STREAMVIZCODES['codes'] 	= ['question','silence','hesitation','laugh','inaudible','break','comment','time']
# deprecated colors, now all set in reanalyse.css
#STREAMVIZCODES['colors'] 	= ['#66CCFF','#BFBD9F','#EC993B','#D9FF00','#ED5300','#ED5300','#517368','#66CCFF']

# ACTIVATED CODES = displayed IN edShow to show/hide, with categories
PARVBCODES={}
PARVBCODES['Transcription'] = 	['break','comment','inaudible','question','time']
PARVBCODES['Verbatim'] = 		['body','directed','hesitation','interruption','laugh','silence']



# THOSE YOU WANT TO PUT SPECIALLY on the margin (will add a css class)
PARVBMARGL = ['comment','break']	# left margin
PARVBMARGR = ['time']				# right margin



########## CODES DEFINITION
# SIMPLE IMAGE
CODES_IMAGE={}
CODES_IMAGE['hesitation']=				'hesitation'
CODES_IMAGE['inaudible']=				'inaudible'
CODES_IMAGE['interruption']=			'interruption'
CODES_IMAGE['part:echo']=				'interruption'
CODES_IMAGE['laugh']=					'laugh'
CODES_IMAGE['silence']=					'silence'
CODES_IMAGE['points de suspension']=	'silence'	# (soon deprecated) more mapping, because some verb of test-studies may contain thoses

# IMAGE WITH TOOLTIP (ie with content)
CODES_IMAGE_TOOLTIP={}
CODES_IMAGE_TOOLTIP['break:']=			'break'
CODES_IMAGE_TOOLTIP['body:']=			'body'
CODES_IMAGE_TOOLTIP['comment:']=		'comment'
CODES_IMAGE_TOOLTIP['directed:']=		'directed'
CODES_IMAGE_TOOLTIP['question:']=		'question'
CODES_IMAGE_TOOLTIP['time:']=			'time'
CODES_IMAGE_TOOLTIP['to:']=				'directed'	# (soon deprecated) more mapping, because some verb of test-studies may contain thoses

# TEXT STYLING
CODES_TEXT={} # text styling (no image no tooltip)
CODES_TEXT['strong:']=			'strong'

# TEXT STYLING WITH TOOLTIP (ie with content)
CODES_TEXT_TOOLTIP={} # text styling (with tooltip)
CODES_TEXT_TOOLTIP['sic:']=				'sic'
CODES_TEXT_TOOLTIP['uncertain:']=		'uncertain'

########## ALL CODES TO CSS CLASSES
CODE_TO_CSS={}
ALLCODES={}
ALLCODES.update(CODES_IMAGE)
ALLCODES.update(CODES_IMAGE_TOOLTIP)
ALLCODES.update(CODES_TEXT)
ALLCODES.update(CODES_TEXT_TOOLTIP)
for k in ALLCODES.values():
	CODE_TO_CSS[k]='text_'+k


########## TREETAGGER CODES
# source:
# http://www.revue-texto.net/Corpus/Publications/Poudat_Taggers.html
CODES_TREETAGGER={}
CODES_TREETAGGER['MISC']={}
CODES_TREETAGGER['MISC']['ABR'] = "abréviations"
CODES_TREETAGGER['MISC']['ADJ'] = "adjectifs"
CODES_TREETAGGER['MISC']['ADV'] = "adverbes"
CODES_TREETAGGER['MISC']['INT'] = "interjections"
CODES_TREETAGGER['MISC']['CON'] = "conjonctions"
CODES_TREETAGGER['MISC']['NOM'] = "noms"
CODES_TREETAGGER['MISC']['NUM'] = "numéraux"
CODES_TREETAGGER['MISC']['NAM'] = "noms propres"
CODES_TREETAGGER['MISC']['PRP'] = "prépositions"
CODES_TREETAGGER['MISC']['PUN'] = "marques de ponctuation"
CODES_TREETAGGER['MISC']['PUN_cit'] = "marques de ponctuation marquant des citations"
CODES_TREETAGGER['MISC']['SENT'] = "phrases"
CODES_TREETAGGER['MISC']['SYM'] = "symboles"

CODES_TREETAGGER['PRONOMS']={}
CODES_TREETAGGER['PRONOMS']['PRO'] = "pronoms"
CODES_TREETAGGER['PRONOMS']['DET_ART'] = "articles"
CODES_TREETAGGER['PRONOMS']['DET_POS'] = "pronoms possessifs"
CODES_TREETAGGER['PRONOMS']['PRO_DEM'] = "pronoms démonstratifs"
CODES_TREETAGGER['PRONOMS']['PRO_IND'] = "pronoms indéfinis"
CODES_TREETAGGER['PRONOMS']['PRO_PER'] = "pronoms personnels"
CODES_TREETAGGER['PRONOMS']['PRO_POS'] = "pronoms possessifs"
CODES_TREETAGGER['PRONOMS']['PRO_REL'] = "pronoms relatifs"
CODES_TREETAGGER['PRONOMS']['PRP_det'] = "déterminants contractés (au,du,aux,des)"

CODES_TREETAGGER['VERBES']={}
CODES_TREETAGGER['VERBES']['VER_cond'] = "verbes au conditionnel"
CODES_TREETAGGER['VERBES']['VER_futu'] = "verbes au futur"
CODES_TREETAGGER['VERBES']['VER_impe'] = "verbes à l'impératif"
CODES_TREETAGGER['VERBES']['VER_impf'] = "verbes à l'imparfait"
CODES_TREETAGGER['VERBES']['VER_infi'] = "verbes à l'infinitif"
CODES_TREETAGGER['VERBES']['VER_pper'] = "participes passés"
CODES_TREETAGGER['VERBES']['VER_ppre'] = "participes présents"
CODES_TREETAGGER['VERBES']['VER_pres'] = "verbes au présent"
CODES_TREETAGGER['VERBES']['VER_simp'] = "verbes au passé simple"
CODES_TREETAGGER['VERBES']['VER_subi'] = "verbes au subjonctif imparfait"
CODES_TREETAGGER['VERBES']['VER_subp'] = "verbes au subjonctif présent"





################################################################################ COLORS
########## COLORS FOR STYLING VERBATIMs (cyclic)
# me
HTML_COLORS=['#FADFCA','#E6F5F3','#FFFDD4','#DEF5DC','#E7E4EB','#c7e9c0','#dadaeb','#d9d9d9','#c6dbef','#fdd0a2']
# http://www.colorhunter.com/tag/pastel/
#removed from next line '#C05253','#D4A9A7','#EC993B','#CF756F'
HTML_COLORS+=['#FFC09D','#FF9987','#FFDC98','#ECC0AF','#F7DCBC','#F3D6CE','#CEA4B0','#F9C49A']
# http://www.hitmill.com/html/pastels.html (there is more)
HTML_COLORS+=['#FFECEC','#FFEEFB','#FFECF5','#FFEEFD','#FDF2FF','#FAECFF','#F1ECFF']
HTML_COLORS+=['#FFECFF','#F4D2F4','#F9EEFF','#F5EEFD','#EFEDFC','#EAF1FB','#DBF0F7']
HTML_COLORS+=['#EEEEFF','#ECF4FF','#F9FDFF','#E6FCFF','#F2FFFE','#CFFEF0','#EAFFEF']
HTML_COLORS+=['#E3FBE9','#F3F8F4','#F1FEED','#E7FFDF','#F2FFEA','#FFFFE3','#FCFCE9']

# Scale from d3.js d3.scale.category20()
#HTML_COLORS=['#aec7e8','#ffbb78','#98df8a','#ff9896','#c5b0d5','#c49c94','#f7b6d2','#c7c7c7','#dbdb8d','#9edae5']

################################################################################ XML
########## NAMESPACES to parse XML
# DDI
XMLDDINMS='{http://www.icpsr.umich.edu/DDI}'
# TEI
XMLTEINMS='{http://www.tei-c.org/ns/1.0}'
XMLNMS ='{http://www.w3.org/XML/1998/namespace}'
# XML TXM
XMLTXM = '{http://textometrie.org/1.0}'
############################################################





############################################################################################################## VISUALIZATIONS
########## ACTIVATED VIZ TYPES (show/hide in evBrowse)
GRAPHTYPES 	= ['Graph_SpeakersSpeakers','Graph_SpeakersWords','Graph_SpeakersAttributes']
VIZTYPES	= GRAPHTYPES + ['Cloud_SolrSpeakerTagCloud','TexteStreamTimeline','Attributes']

########## VIZ DESCRIPTION
# nb: viz description is used to document the viz, not to explain them technically
# to have informations about viz types, see Normalization page

VIZTYPESDESCR = 'Please clic me to update (html) description. If you need general technical information about that viz type, please clic the blue bubble above.'

# VIZTYPESDESCR={}
# VIZTYPESDESCR['Graph_SpeakersSpeakers'] = 		'Speakers Similarities Graph'
# VIZTYPESDESCR['Graph_SpeakersWords'] = 			'Bipart Graph Speakers - Words'
# VIZTYPESDESCR['Graph_SpeakersAttributes'] = 	'Bipart Graph Speakers - Attributes'
# VIZTYPESDESCR['StudyOverview'] = 'aimed to be the main overview viz at study home page'
# VIZTYPESDESCR['Overview'] = 'trying a simple graph overview for left menu facet'
# VIZTYPESDESCR['Attributes'] = '\
# 	Simple display of attributes.<br/>\
# 	Click to see the repartition of other attributes (label is then gray-scaled based on number of speakers).'
# VIZTYPESDESCR['TexteStreamTimeline'] = 	'\
# 	Timeline of speakers interventions and paraverbal. Time(x) is based on number of sentences.<br/>\
# 	Change step value to change sentence-count-interval.'
# VIZTYPESDESCR['Cloud_SolrSpeakerTagCloud'] = '\
# 	<b>Most freq n-grams with tfidf (fetched from solr indexing)</b><br/>\
# 	<b>DF</b> = (normalized) number of speakers using ngram<br/>\
# 	<b>TF</b> = (normalized) ngram count for that speaker >>> <b>GRAY-LEVEL</b><br/>\
# 	<b>TFIDF</b> = TF/DF = specificity of ngram for that speaker >>> <b>SIZE</b><br/>\
# 	NB: we exclude ngrams if [DF=TF=1] OR [included in other longer with same DF,TF]'
########################################################################################################################



