import dash_tabulator
import pandas as pd
import dash


csv_file = 'cost_item_dic.csv'

df = pd.read_csv(csv_file)

df['parent'] = df['parent'].replace({pd.NA: None, float('nan'): None})

data = [{'id': row['id'],
         'parent': row['parent'],
         'name': row['name'],
         'id_1c': row['id_1c'],
         'children': []} for index, row in df.iterrows()]

id_map = {item['id_1c']: item for item in data}

for item in data:
    parent_id = item['parent']
    if parent_id:
        parent_item = id_map.get(parent_id)
        if parent_item:
            parent_item['children'].append(item)

parent_data = [item for item in data if item['parent'] is None]


def tabulator():
    return dash_tabulator.DashTabulator(
        theme="tabulator_midnight",
        id='table',
        columns=[
            {'title': 'Наименование', 'field': 'name'},
        ],
        data=parent_data,
        options={
            "dataTree": True,
            "dataTreeChildField": "children"
        }
    )

