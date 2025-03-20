# Utility functions used across the system
# Provides logging setup and configuration loading
# Common helper functions shared between components

import logging
import yaml

def setup_logging(name, config):
    logger = logging.getLogger(name)
    logger.setLevel(config['logging']['level'])
    
    handler = logging.FileHandler(config['logging']['file'])
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f) 