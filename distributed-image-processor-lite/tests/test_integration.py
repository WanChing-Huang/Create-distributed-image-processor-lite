# Integration tests for the complete system
# Tests end-to-end image processing workflow
# Verifies all components work together correctly

import unittest
import requests
from PIL import Image
from io import BytesIO
from src.coordinator import Coordinator
from src.worker import Worker
from src.frontend import FrontendServer

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.config = {
            'frontend': {'host': 'localhost', 'port': 8000},
            'coordinator': {'host': 'localhost', 'port': 8001},
            'worker': {'host': 'localhost', 'port': 8002, 'threads': 2},
            'storage': {'type': 'local', 'path': './test_storage'},
            'logging': {'level': 'INFO', 'file': 'test.log'}
        }
        
    def test_end_to_end_processing(self):
        # Start all components
        coordinator = Coordinator(self.config)
        worker = Worker(self.config)
        frontend = FrontendServer(self.config)
        
        # Test image processing flow
        test_image = Image.new('RGB', (100, 100), color='red')
        img_byte_arr = BytesIO()
        test_image.save(img_byte_arr, format='JPEG')
        
        response = requests.post(
            'http://localhost:8000/process',
            files={'image': img_byte_arr.getvalue()},
            data={'operation': 'resize', 'width': 50, 'height': 50}
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('task_id', response.json()) 