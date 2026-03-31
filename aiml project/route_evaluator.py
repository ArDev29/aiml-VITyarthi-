import pandas as pd
df = pd.read_csv("data/indian-cities-dataset.csv")
graph ={}
for _,row in df.iterrows():
    u,v,d=row['Origin'], row['Destination'],row['Distance']
    if u not in graph:
        graph[u] = []
    graph[u].append((v,d))

# Depth first search

def dfs(start,end,path=None,visited=None):
    if path == None:
        path=[start]
    if visited==None:
        visited=set()
    if start == end:
        return path
    visited.add(start)
    
    for neighbour,dist in graph.get(start,[]):
        if neighbour not in visited:
            result = dfs(neighbour,end,path+[neighbour],visited)
            if result:
                return result
    return None
        
all_cities = sorted(list(set(df['Origin']).union(set(df['Destination']))))
print("Available Cities:", ", ".join(all_cities))
start_city = input("Enter start city: ").strip().title()
end_city = input("Enter end city: ").strip().title()
result = " -> ".join(dfs(start_city, end_city))
print(f"--- Pathfinding from {start_city} to {end_city} ---")
print(f"DFS Path: {result}")
