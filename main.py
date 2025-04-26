import simulation_engine
import ui_components
import config_loader

def main():
    config = config_loader.load('config.yaml')
    sim = simulation_engine.Simulation(config)
    ui = ui_components.UserInterface(sim, config)
    ui.run_loop()

if __name__ == "__main__":
    main()
