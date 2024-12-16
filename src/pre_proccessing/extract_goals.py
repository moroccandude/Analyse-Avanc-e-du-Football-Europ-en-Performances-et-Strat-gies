import xml.etree.ElementTree as ET
import pandas as pd
from collections import defaultdict
import pandas as pd

def store_goals_to_dataframe(xml_data,a):
    
    
    # Parse the XML data
    root = ET.fromstring(xml_data)
    goals_list = []

    # looper sur value dans xml : <value />
    for value in root.findall('value'):
        goal_data = defaultdict(lambda: None) 

       
        goal_data['goal_id'] = int(value.find('id').text) if value.find('id') is not None else None
        goal_data['team'] = int(value.find('team').text) if value.find('team') is not None else None
        goal_data['player1'] = int(value.find('player1').text) if value.find('player1') is not None else None
        goal_data['player2'] = int(value.find('player2').text) if value.find('player2') is not None else None
        goal_data['elapsed'] = int(value.find('elapsed').text) if value.find('elapsed') is not None else None
        goal_data['goal_type'] = value.find('goal_type').text if value.find('goal_type') is not None else None
        goal_data['goal_subtype'] = value.find('subtype').text if value.find('subtype') is not None else None
        goal_data['goal_comment'] = value.find('comment').text if value.find('comment') is not None else None
        goal_data['event_type'] = int(value.find('event_incident_typefk').text) if value.find('event_incident_typefk') is not None else None
        goal_data['sort_order'] = int(value.find('sortorder').text) if value.find('sortorder') is not None else None
        goal_data['type_goal'] = value.find('type').text if value.find('type') is not None else None
        goal_data['stats'] = value.find('stats') 
        goal_data['match_id']=a
        # dans <stats /> chercher pour columns "goals"  
        if goal_data['stats'] is not None:
            goal_data['goals'] = int(goal_data['stats'].find('goals').text) if goal_data['stats'].find('goals') is not None else None
        else:
            goal_data['goals'] = None
            
        goals_list.append(goal_data)

    goal_df = pd.DataFrame(goals_list)

    return goal_df