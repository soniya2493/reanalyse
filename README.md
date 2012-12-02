Reanalyse
=================================
## absent directories/files
* ./settingsprivate.py
* ./download/
* ./logs/
* ./solrdataindex/
* ./upload/

## Static Html Pages
files are stored within the template/content dir

## django Internationalization how-to
### within template
{% load i18n %}

{% comment %}Translators: Login page title{% endcomment %}

{% trans 'Login Page' %}
### within view
from django.utils.translation import ugettext as _

mystring = _('congratulations')

### translation
required: sudo apt-get install gettext
from django project root, do:
* > sudo django-admin.py makemessages --ignore ./upload --ignore ./media --ignore ./solr -a
* manually translate file /locale/fr/LC_MESSAGES/django.po
* > django-admin.py compilemessages

## solr is based on the default conf (from example), except for
* ./solr/solr/conf/schema.xml defining how models are indexed
* ./solr/solr/conf/solrconfig.xml
 * datadir = ./../solrdataindex/ (temp files)
 * < maxFieldLength >2147483647< /maxFieldLength > (in case of big files)
* ./solr/etc/jetty.xml : if you want to change webserver port
* ./solr/solr/conf/*_fr.txt : stopwords, synonyms, protwords, etc...

## normalisation
![Alt text](http://jiminy.medialab.sciences-po.fr/reanalyse/media/images/content_overview.png "Normalisation")

## django models & views
![Alt text](http://jiminy.medialab.sciences-po.fr/reanalyse/media/images/content_models.png "Django Models")