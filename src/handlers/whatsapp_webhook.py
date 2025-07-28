import os
from flask import Flask, request, jsonify
from src.integrations.whatsapp_bsp_client import send_message
from src.flows.conversation_manager import handle_incoming_message
from src.utils.logger import logger

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    data = request.json
    logger.info(f"Received data: {data}")

    try:
        response = handle_incoming_message(data)
        return jsonify({"status": "ok", "response": response})
    except Exception as e:
        logger.error(f"Error handling webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
