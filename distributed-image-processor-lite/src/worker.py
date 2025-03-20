# Worker component that performs the actual image processing
# Registers with coordinator, receives tasks, and processes images
# Implements work stealing for load balancing

import threading
from PIL import Image
from io import BytesIO
from .communication import TCPClient
from .utils import setup_logging

class Worker:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logging(__name__, config)
        self.coordinator_client = TCPClient(
            config['coordinator']['host'],
            config['coordinator']['port']
        )
        self.tasks = Queue()
        
    def process_image(self, image_data, parameters):
        image = Image.open(BytesIO(image_data))
        # Apply image processing based on parameters
        return image
        
    def start(self):
        self.coordinator_client.send({
            'type': 'worker_register'
        })
        
        for _ in range(self.config['worker']['threads']):
            thread = threading.Thread(target=self._worker_thread)
            thread.daemon = True
            thread.start()
            
    def _worker_thread(self):
        while True:
            task = self.tasks.get()
            result = self.process_image(task['image'], task['parameters'])
            # Send result back to coordinator 