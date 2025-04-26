import unittest
from simulation_engine import Simulation

class TestSimulationLogic(unittest.TestCase):

    def test_initial_state(self):
        config = {}
        sim = Simulation(config)
        self.assertIsNotNone(sim.state)
        self.assertEqual(sim.state['time'], 0)

    def test_update(self):
        config = {}
        sim = Simulation(config)
        sim.update(0.1)
        self.assertEqual(sim.state['time'], 0.1)

if __name__ == '__main__':
    unittest.main()
