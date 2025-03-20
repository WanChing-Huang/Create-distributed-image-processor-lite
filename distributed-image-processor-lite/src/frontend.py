# Frontend server component that provides the HTTP API for image processing requests
# Handles incoming HTTP requests, validates them, and forwards tasks to the coordinator
# Uses Flask for the web server implementation

from flask import Flask, request, jsonify
import requests
from .communication import TCPClient
from .utils import setup_logging

class FrontendServer:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logging(__name__, config)
        self.app = Flask(__name__)
        self.coordinator_client = TCPClient(
            config['coordinator']['host'],
            config['coordinator']['port']
        )
        
        @self.app.route('/process', methods=['POST'])
        def process_image():
            if 'image' not in request.files:
                return jsonify({'error': 'No image provided'}), 400
                
            image = request.files['image']
            task_id = self.coordinator_client.submit_task({
                'image': image.read(),
                'parameters': request.form
            })
            
            return jsonify({'task_id': task_id})
            
    def start(self):
        self.app.run(
            host=self.config['frontend']['host'],
            port=self.config['frontend']['port']
        ) 