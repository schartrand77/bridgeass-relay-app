Home Assistant - Open-WebUI API Relay App 🔄
This app acts as a secure API relay between Open-WebUI and Home Assistant, enabling seamless communication between the two systems. It uses FastAPI and Docker for performance, scalability, and ease of deployment.
📌 Key Features
 Real-time API relay between Open-WebUI and Home Assistant
 Secure authentication via Home Assistant's Long-Lived Access Token 
home_assistant_api_knowledge.md
 Lightweight, production-ready Docker image
 Supports all HTTP methods (GET, POST, PUT, DELETE)
 Easy configuration via environment variables
 📦 Prerequisites
Before deploying, ensure you have:
 Docker and Docker Compose installed
 A running instance of Home Assistant at http://192.168.1.57:8123
 A Long-Lived Access Token generated in Home Assistant
 🚀 Installation
1. Generate a Long-Lived Access Token
 Open Home Assistant in your browser.
 Go to Profile > Developer Tools > Long-Lived Access Tokens.
 Click Add Token, name it, and save it.
 2. Clone the Repository
bash

Collapse
Save
Copy
1
2
git clone https://github.com/schartrand77/bridgeass.git
cd bridgeass
3. Configure Environment Variables
Create a .env file with your Home Assistant details:
env

Collapse
Save
Copy
1
2
HOME_ASSISTANT_URL=http://192.xx.xx:8123
HOME_ASSISTANT_TOKEN=your_long_lived_access_token
4. Build and Run with Docker Compose
bash

Collapse
Save
Copy
1
docker-compose up --build
The app will start on http://localhost:8000.
📱 Usage
This app acts as a proxy, so all API requests to http://localhost:8000/api/... are forwarded to Home Assistant.
Example Requests
1. Get All States
bash

Collapse
Save
Copy
1
curl -X GET "http://localhost:8000/api/states"
2. Turn On a Light
bash

Collapse
Save
Copy
1
2
3
curl -X POST "http://localhost:8000/api/homeassistant/services/light/turn_on" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}'
🛡️ Best Practices
 Never hardcode tokens in code—use environment variables or Docker secrets 
home_assistant_api_knowledge.md
 Validate input in Open-WebUI to avoid misrouting API calls
 Enable HTTPS in production for secure communication
 Backup Home Assistant regularly to prevent data loss
 🧪 Troubleshooting
Error: Error loading ASGI app. Could not import module "relay_app"
 Ensure relay_app.py is in the correct directory (see File Structure ).
 Check that the Dockerfile and docker-compose.yml reference the correct module path.
 📁 File Structure
Ensure your project follows this structure:

Collapse
Save
Copy
1
2
3
4
5
6
relay-app/
├── Dockerfile
├── docker-compose.yml
├── .env
└── relay_app/
    └── relay_app.py
📌 License
This project is licensed under the MIT License. See LICENSE for details.