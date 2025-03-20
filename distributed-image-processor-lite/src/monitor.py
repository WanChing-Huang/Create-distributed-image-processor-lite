# Monitoring component for system metrics collection
# Tracks CPU, memory usage, and custom metrics for each component
# Useful for system health monitoring and debugging

import time
import psutil
from .utils import setup_logging

class Monitor:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logging(__name__, config)
        self.metrics = {}
        
    def update_metrics(self, component_id, metrics):
        self.metrics[component_id] = {
            'timestamp': time.time(),
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            **metrics
        }
        
    def get_metrics(self, component_id=None):
        if component_id:
            return self.metrics.get(component_id)
        return self.metrics 