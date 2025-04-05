Queue Network Simulator (Django)
Overview
Queue Network Simulator is a Django-based web application designed to model and analyze queueing networks. This simulator allows users to simulate various types of queuing systems, manage configurations via a web interface, and evaluate their performance. It is built with flexibility in mind, enabling users to define custom network topologies, service rates, and arrival processes.
The tool is primarily useful for studying and optimizing performance in networked systems, including computer networks, telecommunications, and service systems.
Features
- Simulate multiple types of queues (e.g., M/M/1, M/M/c, etc.)
- Customizable network topologies and configurations through a web interface
- Configurable arrival rates, service rates, and buffer sizes
- Performance metrics, such as waiting time, throughput, and utilization
- Visualizations of queueing networks and their states over time
- Statistical analysis and reporting
- User authentication and role-based access
Requirements
To run this Django-based simulator, you will need the following:
- Python 3.x
- Django
- NumPy
- Matplotlib (for visualizations)
- SimPy (for discrete-event simulation)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
Installation
Follow these steps to install the Queue Network Simulator Django project:

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

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

You can now access the application in your browser at `http://127.0.0.1:8000/`.
Usage
Running the Simulator
After starting the Django development server, you can access the Queue Network Simulator through the web interface. The simulator allows you to create network configurations, specify arrival rates, service rates, and buffer sizes. You can visualize the performance of your system and evaluate metrics such as waiting time and throughput.
Example Command
For a custom simulation with specific parameters, you can interact with the web interface to adjust the simulation settings. You can also modify configurations in the Django admin interface if needed.
Configuration File
You can configure your simulation using the web interface or directly via the Django admin panel. Network topologies, arrival rates, service rates, and other parameters can be set up through these interfaces.
Visualization
The simulator includes built-in visualization tools to plot the system's behavior over time. After running a simulation, the results will be displayed in graphical form, providing insights into the queueing system's performance.
Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request.
License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Acknowledgments
- [SimPy](https://simpy.readthedocs.io/en/latest/) - For discrete-event simulation
- [Matplotlib](https://matplotlib.org/) - For data visualization
- [Django](https://www.djangoproject.com/) - For the web framework
