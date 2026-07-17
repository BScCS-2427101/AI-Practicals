import heapq
import matplotlib.pyplot as plt

# =====================================================================
# 1. STRUCTURAL DATA & SEPARATED HEURISTICS
# =====================================================================

road_network = {
    'MVLU': {'Bandra': (12, 22), 'Sion': (14, 30)},
    'Bandra': {'Worli': (6, 12), 'Byculla': (10, 25)},
    'Sion': {'Byculla': (13, 32)},
    'Worli': {'CSMT': (9, 16)},
    'Byculla': {'CSMT': (6, 18)},
    'CSMT': {'Gateway': (3, 5)},
    'Gateway': {}
}

time_heuristics = {'MVLU': 55, 'Bandra': 33, 'Sion': 50, 'Worli': 21, 'Byculla': 23, 'CSMT': 5, 'Gateway': 0}
dist_heuristics = {'MVLU': 22, 'Bandra': 14, 'Sion': 13, 'Worli': 9, 'Byculla': 7, 'CSMT': 2, 'Gateway': 0}

map_coordinates = {
    'MVLU': (2.0, 6.0), 
    'Bandra': (0.8, 4.5),   
    'Sion': (3.2, 4.5),     
    'Worli': (0.3, 3.0),    
    'Byculla': (2.2, 3.0),  
    'CSMT': (2.0, 1.5), 
    'Gateway': (2.0, 0.2)
}

# =====================================================================
# 2. ALGO 1: A* SEARCH (TIME OPTIMIZED)
# =====================================================================

def compute_a_star_time(graph, h_map, start, goal):
    fringe = [(h_map[start], start, [start], 0, 0)]  
    settled = set()
    steps = 0
    
    while fringe:
        f_val, current, route, g_time, g_dist = heapq.heappop(fringe)
        steps += 1
        if current == goal:
            return route, g_time, g_dist, steps
            
        if current in settled:
            continue
        settled.add(current)
        
        for neighbor, (d_cost, t_cost) in graph[current].items():
            if neighbor not in settled:
                heapq.heappush(fringe, (g_time + t_cost + h_map[neighbor], neighbor, 
                                       route + [neighbor], g_time + t_cost, g_dist + d_cost))
    return None, 0, 0, steps

# =====================================================================
# 3. ALGO 2: RBFS (DISTANCE OPTIMIZED)
# =====================================================================

def compute_rbfs_distance(graph, h_map, start, goal):
    def evaluate(node, current_d, current_t, f_limit, path, metrics):
        metrics['steps'] += 1
        if node == goal:
            return True, path, current_d, current_t, current_d
            
        neighbors = graph[node]
        if not neighbors:
            return False, [], 0, 0, float('inf')
            
        successors = []
        for adjacent, (d_cost, t_cost) in neighbors.items():
            if adjacent not in path:
                next_d = current_d + d_cost
                next_t = current_t + t_cost
                next_f = max(next_d + h_map[adjacent], current_d + h_map[node])
                successors.append([next_f, adjacent, next_d, next_t])
                
        if not successors:
            return False, [], 0, 0, float('inf')
            
        while True:
            successors.sort(key=lambda x: x[0])
            best = successors[0]
            if best[0] > f_limit:
                return False, [], 0, 0, best[0]
            alt_f = successors[1][0] if len(successors) > 1 else float('inf')
            
            success, final_p, final_d, final_t, back_f = evaluate(
                best[1], best[2], best[3], min(f_limit, alt_f), path + [best[1]], metrics
            )
            best[0] = back_f
            if success:
                return True, final_p, final_d, final_t, back_f

    run_metrics = {'steps': 0}
    _, route, d_cost, t_cost, _ = evaluate(start, 0, 0, float('inf'), [start], run_metrics)
    return route, d_cost, t_cost, run_metrics['steps']

# =====================================================================
# 4. HIGH-CONTRAST VISUALIZATION ENGINE
# =====================================================================

def draw_map_graph(title, graph, h_map, coords, active_path, total_time, total_dist, highlight_color):
    plt.figure(figsize=(9.5, 7.5))
    
    # 1. Render Path Edges
    for location, connections in graph.items():
        x1, y1 = coords[location]
        for target, (dist, time) in connections.items():
            x2, y2 = coords[target]
            
            on_path = (location in active_path and target in active_path and 
                       active_path.index(target) == active_path.index(location) + 1)
            
            line_color = highlight_color if on_path else '#d2d7d9'
            line_thick = 5.0 if on_path else 1.5
            z_order = 2 if on_path else 1
            
            plt.plot([x1, x2], [y1, y2], color=line_color, linewidth=line_thick, zorder=z_order)
            
            label_text = f"{dist}km / {time}m"
            plt.text((x1 + x2) / 2, (y1 + y2) / 2, label_text, color='#c0392b' if on_path else '#7f8c8d', 
                     fontsize=8, fontweight='bold' if on_path else 'normal', ha='center', va='center',
                     bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1.5))
            
    # 2. Render Nodes
    for location, (x, y) in coords.items():
        is_active = location in active_path
        node_color = highlight_color if is_active else '#34495e'
        scale = 1300 if is_active else 900
        
        plt.scatter(x, y, color=node_color, s=scale, zorder=3, edgecolor='black', linewidth=1)
        plt.text(x, y, f"{location}\nh={h_map[location]}", ha='center', va='center', 
                 color='white', fontsize=8, fontweight='bold')
        
    plt.title(f"{title}\nHighlighted Journey metrics: {total_dist} km | {total_time} mins", fontsize=12, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()

def draw_comparison_chart(a_path_len, a_steps, r_path_len, r_steps):
    """Generates a structured side-by-side comparison chart matching graph realities."""
    plt.figure(figsize=(8, 5.5))
    
    categories = ['A* (Time-Optimized)', 'RBFS (Dist-Optimized)']
    x = [0, 1]
    width = 0.25
    
    # Plot Path length nodes vs Exploratory processing metrics side by side
    bars_path = plt.bar([pos - width/2 for pos in x], [a_path_len, r_path_len], width=width, label='Nodes in Final Path', color='#3498db', edgecolor='black')
    bars_steps = plt.bar([pos + width/2 for pos in x], [a_steps, r_steps], width=width, label='Total Expansion Steps', color='#e74c3c', edgecolor='black')
    
    plt.xticks(x, categories, fontweight='bold')
    plt.ylabel('Node Quantification Metric Value', fontsize=10, fontweight='bold')
    plt.title('Performance Comparison: Final Path Nodes vs Evaluation Steps', fontsize=11, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.legend(loc='upper left')
    
    # Text labels over the bars
    for bar in bars_path + bars_steps:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.2, str(yval), ha='center', va='bottom', fontweight='bold', fontsize=9)
        
    plt.tight_layout()

# =====================================================================
# 5. EXECUTION
# =====================================================================

if __name__ == "__main__":
    start_node, end_node = 'MVLU', 'Gateway'
    
    a_route, a_time, a_dist, a_steps = compute_a_star_time(road_network, time_heuristics, start_node, end_node)
    r_route, r_dist, r_time, r_steps = compute_rbfs_distance(road_network, dist_heuristics, start_node, end_node)
    
    # Extract structural length arrays from path outputs
    a_path_len = len(a_route)
    r_path_len = len(r_route)
    
    # --- GRAPH 1: A* Time Optimized Map ---
    draw_map_graph("Graph 1: A* Search (Optimized for Fastest Time)", 
                   road_network, time_heuristics, map_coordinates, a_route, a_time, a_dist, '#2ecc71')
    
    # --- GRAPH 2: RBFS Distance Optimized Map ---
    draw_map_graph("Graph 2: Recursive Best-First Search (Optimized for Shortest Distance)", 
                   road_network, dist_heuristics, map_coordinates, r_route, r_time, r_dist, '#e67e22')
    
    # --- GRAPH 3: Dynamic Dual Metric Bar Chart ---
    draw_comparison_chart(a_path_len, a_steps, r_path_len, r_steps)
    
    plt.show()
