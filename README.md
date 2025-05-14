# 🔄 Home Assistant ↔ Open-WebUI API Relay

A secure, lightweight, and production-ready FastAPI relay service that enables seamless, real-time API communication between Open-WebUI and Home Assistant. This app simplifies the integration between your smart home and AI interface, using Docker for scalability and ease of deployment.

---

## 🚀 Features

- 🔄 **Real-time API relay** between Open-WebUI and Home Assistant  
- 🔐 **Secure authentication** using Home Assistant's Long-Lived Access Tokens  
- 📦 **Lightweight Dockerized app** built for performance and easy deployment  
- 📡 **Supports all HTTP methods**: `GET`, `POST`, `PUT`, `DELETE`  
- ⚙️ **Simple configuration** via environment variables  

---

## 🧰 Prerequisites

Before deploying, make sure you have:

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) installed  
- A running instance of Home Assistant (e.g. `http://<HOME_ASSISTANT_URL>:<PORT>`)  
- A Long-Lived Access Token from Home Assistant  
  - Go to: **Profile → Developer Tools → Long-Lived Access Tokens**
  - Click **"Create Token"**, give it a name, and save it securely  

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-repo/relay-app.git
cd relay-app
```

2. **Create `.env` File**

Create a `.env` file in the project root with your Home Assistant details:

```env
HOME_ASSISTANT_URL=http://<HOME_ASSISTANT_URL>:<PORT>
HOME_ASSISTANT_TOKEN=your_long_lived_access_token
```

3. **Build and Run the App**

```bash
docker-compose up --build
```

The app will be available at:  
**http://localhost:8000**

---

## 📱 Usage

This app acts as a reverse proxy, forwarding API requests from Open-WebUI to Home Assistant.

### Example Requests

**1. Get All States**

```bash
curl -X GET "http://localhost:8000/api/states"
```

**2. Turn On a Light**

```bash
curl -X POST "http://localhost:8000/api/homeassistant/services/light/turn_on" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}'
```

---

## 🛡️ Best Practices

- ❌ **Never hardcode tokens**—use environment variables or Docker secrets  
- ✅ **Validate input** in Open-WebUI to prevent API misrouting  
- 🔒 **Enable HTTPS** in production environments  
- 💾 **Regularly back up** your Home Assistant instance  

---

## 🧪 Troubleshooting

**Error:** `Error loading ASGI app. Could not import module "relay_app"`  
- Confirm `relay_app.py` is located in `relay_app/`  
- Verify the `Dockerfile` and `docker-compose.yml` reference the correct module path  

---

## 📁 Project Structure

```
relay-app/
├── Dockerfile
├── docker-compose.yml
├── .env
└── relay_app/
    └── relay_app.py
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).