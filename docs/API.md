# Elimuhub Messaging Service API

## Endpoints

### `POST /webhook`

Receives incoming WhatsApp messages from the BSP and triggers business logic.

#### Request Example

```json
{
  "message": "I want to know about admission",
  "from": "+254700000000"
}
