from http import HTTPStatus
from albert import Item, UrlAction
import requests
from os.path import dirname
from xml.etree import *

__title__       = "Drupal API"
__version__     = "0.0.1"
__authors__     = "0xfad"
__triggers__    = "drapi "

iconPath = dirname(__file__)+"/drupal.png"
searchURL = "https://api.drupal.org/index.php?q=api/search/autocomplete/102/{0}"
resultURL = "https://api.drupal.org/search/site/?q={0}"

def handleQuery(query):
    if not query.isTriggered:
        return

    query.disableSort()

    response = requests.get(searchURL.format(query.string))
    if response.status_code != HTTPStatus.OK:
        return []

    items = []
    for key in response.json():
        item = Item(
            id = key, 
            text = key, 
            icon = iconPath,
            subtext = "[No Description]"
        )
        item.addAction(UrlAction("Open %s" % key, resultURL.format(key)))
        items.append(item)

    return items
