# Storage component for handling image data persistence
# Provides basic file system storage operations for processed images
# Can be extended to support different storage backends

import os
from .utils import setup_logging

class Storage:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logging(__name__, config)
        self.storage_path = config['storage']['path']
        os.makedirs(self.storage_path, exist_ok=True)
        
    def save(self, task_id, data):
        path = os.path.join(self.storage_path, f"{task_id}.jpg")
        with open(path, 'wb') as f:
            f.write(data)
        return path
        
    def load(self, task_id):
        path = os.path.join(self.storage_path, f"{task_id}.jpg")
        with open(path, 'rb') as f:
            return f.read() 