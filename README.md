# Elimuhub Messaging Service

A robust, open-source messaging service designed for Elimuhub Education Consultants to automate communication with students, parents, and institutions using WhatsApp via a free/low-cost Business Solution Provider (BSP).  
This repository enables structured, secure, and scalable messaging logic, with modular code for easy extension and integration.

## Features

- Send and receive WhatsApp messages via BSP APIs (AiSensy, YCloud, Interakt, etc.)
- Message templates for admissions, reminders, support, and more
- Webhook handling for incoming WhatsApp messages
- Conversation management logic (flows)
- Modular architecture: handlers, integrations, templates, utils, config
- Secure: uses environment variables for API keys and config
- Unit and integration tests
- Ready for CI/CD with GitHub Actions
- Extensible for in-app/internal chat (Rocket.Chat, Mattermost, etc.)

---

## Directory Structure

```
elimuhub-messaging-service/
├── README.md
├── .env.example
├── config/
│   └── default.yaml
├── src/
│   ├── handlers/
│   │   └── whatsapp_webhook.py
│   ├── integrations/
│   │   └── whatsapp_bsp_client.py
│   ├── templates/
│   │   └── admission_template.json
│   ├── utils/
│   │   └── logger.py
│   └── flows/
│       └── conversation_manager.py
├── tests/
│   ├── test_whatsapp_webhook.py
│   └── test_bsp_client.py
├── docs/
│   ├── API.md
│   └── DEPLOYMENT.md
├── .github/
│   └── workflows/
│       └── ci.yml
```

---

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/kibiti/elimuhub-messaging-service.git
   cd elimuhub-messaging-service
   ```

2. **Configure environment variables**
   - Copy `.env.example` to `.env` and fill in your BSP API credentials and settings.

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the service**
   ```bash
   python src/handlers/whatsapp_webhook.py
   ```

5. **Run tests**
   ```bash
   pytest tests/
   ```

---

## Example WhatsApp Template

See [`src/templates/admission_template.json`](src/templates/admission_template.json) for a sample admissions notification template.

---

## Documentation

- [API Reference](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Using Message Templates](src/templates/README.md)

---

## Contribution

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

---

## License

MIT License

---

## Links

- [Live Demo (mock)](https://github.com/kibiti/elimuhub-messaging-service)
- [API Documentation](docs/API.md)
- [Sample Admission Template](src/templates/admission_template.json)

```
