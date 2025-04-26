class Simulation:
    def __init__(self, config):
        self.state = {}
        self.agents = []
        self.config = config
        self._load_initial_state()

    def _load_initial_state(self):
        # Initialize simulation state
        self.state['time'] = 0
        self.state['agents'] = []

    def update(self, delta_time):
        # Update simulation state
        self.state['time'] += delta_time
        # Update agents logic here

    def get_state_snapshot(self):
        return self.state
