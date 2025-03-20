# Unit tests for core system components
# Tests initialization and basic functionality of coordinator and worker
# Ensures core components are working as expected

import unittest
from src.coordinator import Coordinator
from src.worker import Worker
from src.frontend import FrontendServer

class TestCore(unittest.TestCase):
    def setUp(self):
        self.config = {
            'frontend': {'host': 'localhost', 'port': 8000},
            'coordinator': {'host': 'localhost', 'port': 8001},
            'worker': {'host': 'localhost', 'port': 8002, 'threads': 2},
            'storage': {'type': 'local', 'path': './test_storage'},
            'logging': {'level': 'INFO', 'file': 'test.log'}
        }
        
    def test_coordinator_initialization(self):
        coordinator = Coordinator(self.config)
        self.assertIsNotNone(coordinator.task_queue)
        
    def test_worker_initialization(self):
        worker = Worker(self.config)
        self.assertIsNotNone(worker.coordinator_client) 