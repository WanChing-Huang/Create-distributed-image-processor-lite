# Main entry point for the distributed image processor
# Handles command line arguments and starts the appropriate component (frontend, coordinator, or worker)
# based on the specified role

import argparse
import yaml
from src.frontend import FrontendServer
from src.coordinator import Coordinator
from src.worker import Worker

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description='Distributed Image Processor')
    parser.add_argument('--role', choices=['frontend', 'coordinator', 'worker'],
                       required=True, help='Role of this instance')
    parser.add_argument('--config', default='config.yaml',
                       help='Path to configuration file')
    
    args = parser.parse_args()
    config = load_config(args.config)
    
    if args.role == 'frontend':
        server = FrontendServer(config)
        server.start()
    elif args.role == 'coordinator':
        coordinator = Coordinator(config)
        coordinator.start()
    elif args.role == 'worker':
        worker = Worker(config)
        worker.start()

if __name__ == '__main__':
    main() 