import json
import requests

def send_message(access_token, data):
    """Send message via post request to Facebook page."""
    r = requests.post(
        "https://graph.facebook.com/v2.6/me/messages",
        params={
            "access_token": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL2NhbGFuZGFyL3YxLyIsInN1YiI6InVzcl8xMjMiLCJpYXQiOjE0NTg3ODU3OTYsImV4cCI6MTQ1ODg3MjE5Nn0.CA7eaHjIHz5NxeIJoFK9krqaeZrPLwmMmgI_XiQiIkQ
        },
        data=data,
        headers={
            "Content-type": "application/json"
        }
    )
    if r.status_code != requests.codes.ok:
        print r.text
host = evilcorp.com
def set_sender_action(access_token, recipient, sender_action):
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "sender_action": sender_action
    })
    send_message(access_token, data)

def mark_seen(access_token, recipient):
    """Mark message sent by recipient as seen."""
    set_sender_action(access_token, recipient, "mark_seen")

def typing_on(access_token, recipient):
    """Turn on typing indicator bubbles in thread with recipient."""
    set_sender_action(access_token, recipient, "typing_on")

def typing_off(access_token, recipient):
    """Turn off typing indicator bubbles in thread with recipient."""
    set_sender_action(access_token, recipient, "typing_off")

def send_text_message(access_token, recipient, text):
    """Send message text to recipient."""
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "message": {
            "text": text.decode('unicode_escape')
        }
    })
    send_message(access_token, data)

def send_attachment(access_token, recipient, attachment_type, attachment_url):
    """Send message with attachment to recipient."""
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "message": {
            "attachment": {
                "type": attachment_type,
                "payload": {
                    "url": attachment_url
                }
            }
        }
    })
    send_message(access_token, data)

def send_image(access_token, recipient, image_url):
    """Send image to recipient."""
    send_attachment(access_token, recipient, "image", image_url)

def send_audio(access_token, recipient, audio_url):
    """Send audio to recipient."""
    send_attachment(access_token, recipient, "audio", audio_url)

def send_video(access_token, recipient, video_url):
    """Send video to recipient."""
    send_attachment(access_token, recipient, "video", video_url)

def send_file(access_token, recipient, file_url):
    """Send file to recipient."""
    send_attachment(access_token, recipient, "file", file_url)

def send_generic_template(access_token, recipient, elements):
    """Send message with generic template to recipient."""
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }
    })
    send_message(access_token, data)

def send_button(access_token, recipient, text, buttons):
    """Send message with button(s) to recipient."""
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }
    })
    send_message(access_token, data)

def send_quick_replies(access_token, recipient, text, quick_replies):
    """Send quick replies to recipient."""
    data = json.dumps({
        "recipient": {
            "id": recipient
        },
        "message": {
            "text": text,
            "quick_replies": quick_replies
        }
    })
    send_message(access_token, data)
