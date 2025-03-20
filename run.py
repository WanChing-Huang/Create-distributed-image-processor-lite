import yaml
import logging
from src.frontend import Frontend
from src.coordinator import Coordinator
from src.worker import Worker
from src.monitor import Monitor
import multiprocessing as mp

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def setup_logging(config):
    logging.basicConfig(
        level=config['monitoring']['log_level'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    config = load_config()
    setup_logging(config)
    
    # Start monitor
    monitor = Monitor(config)
    monitor_process = mp.Process(target=monitor.run)
    monitor_process.start()
    
    # Start coordinator
    coordinator = Coordinator(config)
    coordinator_process = mp.Process(target=coordinator.run)
    coordinator_process.start()
    
    # Start workers
    workers = []
    for i in range(config['processing']['max_workers']):
        worker = Worker(config, worker_id=i)
        worker_process = mp.Process(target=worker.run)
        worker_process.start()
        workers.append(worker_process)
    
    # Start frontend
    frontend = Frontend(config)
    frontend.run()

if __name__ == '__main__':
    main()
