import xml.etree.ElementTree as ET
import pandas as pd

def extract_possession(xml_data, a):
    root = ET.fromstring(xml_data)
    
    # List to store parsed data
    possession_data = []
    
    for value in root.findall('value'):
        possession_data.append({
            'comment': value.find('comment').text if value.find('comment') is not None else None,
            'event_incident_typefk': value.find('event_incident_typefk').text if value.find('event_incident_typefk') is not None else None,
            'elapsed': value.find('elapsed').text if value.find('elapsed') is not None else None,
            'elapsed_plus': value.find('elapsed_plus').text if value.find('elapsed_plus') is not None else None,
            'subtype': value.find('subtype').text if value.find('subtype') is not None else None,
            'sortorder': value.find('sortorder').text if value.find('sortorder') is not None else None,
            'awaypos': value.find('awaypos').text if value.find('awaypos') is not None else None,
            'homepos': value.find('homepos').text if value.find('homepos') is not None else None,
            'n': value.find('n').text if value.find('n') is not None else None,
            'type': value.find('type').text if value.find('type') is not None else None,
            'id': value.find('id').text if value.find('id') is not None else None,
            'id_match': a,  # Add match ID as in previous code
        })
    
    element_possession = pd.DataFrame(possession_data)
    return element_possession

possession_No_Nan = df_matchs.dropna(subset=['possession'])

possession_table = []

for index, value in enumerate(possession_No_Nan['possession']):
    possession_table.append(extract_possession(value, possession_No_Nan.index[index]))  # Use the correct index

final_possession_table = pd.concat(possession_table, ignore_index=True)

# print(final_possession_table.head())