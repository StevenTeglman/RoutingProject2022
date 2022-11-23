import csv
header = ['algorithm', 'graph_preset_number', 'elapsed_time']
data = [
        {'algorithm': 'dijkstra',  'graph_preset_number': 1, 'elapsed_time':0.5377322140011529},
        {'algorithm': 'a_star',  'graph_preset_number': 1, 'elapsed_time':7.670558501002233},
        {'algorithm': 'bfs',  'graph_preset_number': 1, 'elapsed_time':0.22938291299942648},
        # {'algorithm': 'dfs', 'graph_preset_number': 1, 'elapsed_time':},
        {'algorithm': 'greedy best-first search',  'graph_preset_number': 1, 'elapsed_time':4.795463894999557},

        {'algorithm': 'dijkstra',  'graph_preset_number': 2, 'elapsed_time':0.5097170600020036},
        {'algorithm': 'a_star',  'graph_preset_number': 2, 'elapsed_time':3.472584202001599},
        {'algorithm': 'bfs',  'graph_preset_number': 2, 'elapsed_time':0.4118758090007759},
        {'algorithm': 'dfs',  'graph_preset_number': 2, 'elapsed_time':6.369991751853377e-07},
        {'algorithm': 'greedy best-first search',  'graph_preset_number': 2, 'elapsed_time':2.483678732998669},

        {'algorithm': 'dijkstra',  'graph_preset_number': 3, 'elapsed_time':0.5074079330006498},
        {'algorithm': 'a_star',  'graph_preset_number': 3, 'elapsed_time':4.676429063998512},
        {'algorithm': 'bfs',  'graph_preset_number': 3, 'elapsed_time':0.22364121400096337},
        # {'algorithm': 'dfs',  'graph_preset_number': 3, 'elapsed_time':},
        {'algorithm': 'greedy best-first search',  'graph_preset_number': 3, 'elapsed_time':3.5205514519984717}
        ]
with open('metric.csv', 'w') as file:
    # Create a CSV dictionary writer and add the student header as field names
    writer = csv.DictWriter(file, fieldnames=header)
    # Use writerows() not writerow()
    writer.writeheader()
    writer.writerows(data)