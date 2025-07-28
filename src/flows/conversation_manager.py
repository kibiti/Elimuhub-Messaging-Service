from src.integrations.whatsapp_bsp_client import send_message

def handle_incoming_message(data):
    # Example logic: reply to admissions inquiries with a template
    message = data.get("message", "").lower()
    user_phone = data.get("from")
    
    if "admission" in message:
        template_name = "admission_template"
        template_params = [
            {"type": "text", "text": "Student Name"},
            {"type": "text", "text": "University Name"},
            {"type": "text", "text": "Accepted"},
            {"type": "text", "text": "https://elimuhub.com/details"}
        ]
        send_message(user_phone, template_name, template_params)
        return "Admission template sent."
    return "No action taken."
