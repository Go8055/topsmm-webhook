from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8616956712:AAFbRYz9y180q2n6anra4kf3rgbhvNyMuFc"
CHAT_ID = "1604645262"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return "No data", 400
    
    order_id = data.get('order_id', 'N/A')
    service = data.get('service', 'N/A')
    quantity = data.get('quantity', 'N/A')
    link = data.get('link', 'N/A')
    charge = data.get('charge', 'N/A')
    status = data.get('status', 'N/A')

    message = f"""
🛒 *Naya Order Aaya!*

🆔 Order ID: `{order_id}`
📦 Service: `{service}`
🔢 Quantity: `{quantity}`
🔗 Link: `{link}`
💰 Charge: `{charge}`
📊 Status: `{status}`
"""
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    )
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
