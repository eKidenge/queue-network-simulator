from django.shortcuts import render
from .forms import SimulationForm
import random
from collections import deque, defaultdict

def simulate_network(customers, time_steps):
    nodes = {
        'A': {'rate': 5, 'queue': deque(), 'next': [('B', 0.3), ('C', 0.7)]},
        'B': {'rate': 3, 'queue': deque(), 'next': [('C', 0.5), ('D', 0.5)]},
        'C': {'rate': 4, 'queue': deque(), 'next': [('D', 0.4), ('A', 0.6)]},
        'D': {'rate': 2, 'queue': deque(), 'next': [('A', 1.0)]},
    }

    cust = {i: {'node': random.choice(list(nodes)), 'time': 0} for i in range(customers)}
    for cid, info in cust.items():
        nodes[info['node']]['queue'].append(cid)

    queue_lengths = defaultdict(list)
    busy_time = defaultdict(int)

    for t in range(time_steps):
        for node, info in nodes.items():
            q = info['queue']
            rate = info['rate']
            queue_lengths[node].append(len(q))

            for _ in range(min(rate, len(q))):
                cid = q.popleft()
                cust[cid]['time'] += 1
                busy_time[node] += 1

                next_node = random.choices([n for n, _ in info['next']],
                                           weights=[p for _, p in info['next']])[0]
                cust[cid]['node'] = next_node
                nodes[next_node]['queue'].append(cid)

        for cid in cust:
            cust[cid]['time'] += 1

    avg_queues = {node: round(sum(lengths)/len(lengths), 2) for node, lengths in queue_lengths.items()}
    utilization = {node: round(busy_time[node]/time_steps, 2) for node in nodes}
    avg_time = round(sum(c['time'] for c in cust.values()) / customers, 2)

    return avg_queues, utilization, avg_time

def index(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['customers']
            steps = form.cleaned_data['time_steps']
            avg_queues, utilization, avg_time = simulate_network(cust, steps)
            return render(request, 'simulator/results.html', {
                'queues': avg_queues,
                'utilization': utilization,
                'avg_time': avg_time,
            })
    else:
        form = SimulationForm()
    return render(request, 'simulator/index.html', {'form': form})
