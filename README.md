Queue Network Simulator
Overview
Queue Network Simulator is a Python-based simulation tool designed to model and analyze queueing networks. This simulator allows users to simulate various types of queuing systems and evaluate their performance. It is built with flexibility in mind, enabling users to define custom network topologies, service rates, and arrival processes.
The tool is primarily useful for studying and optimizing performance in networked systems, including computer networks, telecommunications, and service systems.
Features
- Simulate multiple types of queues (e.g., M/M/1, M/M/c, etc.)
- Customizable network topologies and configurations
- Configurable arrival rates, service rates, and buffer sizes
- Performance metrics, such as waiting time, throughput, and utilization
- Visualizations of queueing networks and their states over time
- Statistical analysis and reporting
Requirements
To run this simulator, you will need the following:
- Python 3.x
- NumPy
- Matplotlib (for visualizations)
- SimPy (for discrete-event simulation)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
Installation
Follow these steps to install the Queue Network Simulator:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/eKidenge/queue-network-simulator.git
```

2. Navigate to the project directory:

```bash
cd queue-network-simulator
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
Usage
Running the Simulator
To run the simulator, use the following command:

```bash
python main.py
```

This will initiate the simulation with default parameters. You can modify the configuration in the script or pass custom parameters via command line arguments.
Example Command
For a custom simulation with specific parameters, you can modify the script or run:

```bash
python main.py --arrival_rate 2 --service_rate 5 --num_servers 3
```

This command will simulate a system with:
- Arrival rate of 2 customers per unit time
- Service rate of 5 customers per unit time
- 3 servers in the queue
Configuration File
You can also configure your simulation using a configuration file (e.g., `config.json`). This file allows you to define the network topology, parameters, and simulation settings.
Visualization
The simulator includes built-in visualization tools to plot the system's behavior over time. After running a simulation, the results will be displayed in graphical form.
Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request.
License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Acknowledgments
- [SimPy](https://simpy.readthedocs.io/en/latest/) - For discrete-event simulation
- [Matplotlib](https://matplotlib.org/) - For data visualization
