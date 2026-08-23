import requests

from django.conf import settings


def send_whatsapp_message(
    phone_number,
    message
):

    token = settings.WHATSAPP_ACCESS_TOKEN
    phone_number_id = settings.WHATSAPP_PHONE_NUMBER_ID
    api_version = settings.WHATSAPP_API_VERSION

    if not token or not phone_number_id:
        print("WhatsApp API credentials are missing.")
        return False

    # Remove + and spaces
    phone_number = (
        phone_number
        .replace("+", "")
        .replace(" ", "")
        .replace("-", "")
    )

    url = (
        f"https://graph.facebook.com/"
        f"{api_version}/"
        f"{phone_number_id}/messages"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": message,
        },
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=15
        )

        print(
            "WhatsApp response:",
            response.status_code,
            response.text
        )

        return response.ok

    except requests.RequestException as e:

        print(
            "WhatsApp API error:",
            str(e)
        )

        return False


def build_order_message(
    customer_name,
    order_id,
    items,
    subtotal,
    shipping,
    grand_total,
    delivery_method,
    address,
    city,
    state,
    pincode,
    country
):

    item_lines = []

    for item in items:

        item_lines.append(
            f"• {item['title']} "
            f"x {item['quantity']} "
            f"— ₹{item['total']}"
        )

    items_text = "\n".join(item_lines)

    message = f"""
🏛️ *NUMIS — ORDER CONFIRMED*

Hello {customer_name},

Thank you for purchasing from NUMIS.

━━━━━━━━━━━━━━━━━━

📦 *ORDER #{order_id}*

*COLLECTIBLES*

{items_text}

━━━━━━━━━━━━━━━━━━

💰 *PAYMENT SUMMARY*

Subtotal: ₹{subtotal}
Shipping: ₹{shipping}
Grand Total: ₹{grand_total}

━━━━━━━━━━━━━━━━━━

🚚 *DELIVERY*

Method: {delivery_method}

📍 *SHIPPING ADDRESS*

{address}
{city}, {state}
{pincode}
{country}

━━━━━━━━━━━━━━━━━━

🔐 Your collectible will be authenticated and securely packaged before dispatch.

Thank you for choosing NUMIS.

— NUMIS Collections
"""

    return message.strip()