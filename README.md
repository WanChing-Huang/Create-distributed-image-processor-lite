Distributed Image Processor Lite

A lightweight distributed system for processing images across multiple worker nodes with load balancing and work stealing capabilities.

## Features
- Distributed image processing across multiple workers
- Load balancing and work stealing
- Fault tolerance and failover handling
- Basic monitoring and metrics
- TCP/IP-based communication

## Setup
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure the system in `config.yaml`

3. Run the system:

```bash
python run.py
```

## Architecture
- Frontend: API handling and load balancing
- Coordinator: Task distribution and failover
- Workers: Image processing with work stealing
- Storage: File operations
- Monitor: System metrics and monitoring

## Configuration
Edit `config.yaml` to configure:
- Network settings
- Storage paths
- Processing parameters
- Monitoring options


