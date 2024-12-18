import xml.etree.ElementTree as ET
import pandas as pd

def extract_yellow_cart(xml_data, a):
    root = ET.fromstring(xml_data)
    
    card_list = []
    
    for card in root.findall(".//value"):
        card_data = {}
        
        card_data['comment'] = card.findtext('comment')
        card_data['ycards'] = card.findtext('.//ycards')
        card_data['event_incident_typefk'] = card.findtext('event_incident_typefk')
        card_data['elapsed'] = card.findtext('elapsed')
        card_data['card_type'] = card.findtext('card_type')
        card_data['subtype'] = card.findtext('subtype')
        card_data['player1'] = card.findtext('player1')
        card_data['sortorder'] = card.findtext('sortorder')
        card_data['team'] = card.findtext('team')
        card_data['n'] = card.findtext('n')
        card_data['type'] = card.findtext('type')
        card_data['id'] = card.findtext('id')
        card_data['id_match'] = a
        card_list.append(card_data)
    
    return pd.DataFrame(card_list)
