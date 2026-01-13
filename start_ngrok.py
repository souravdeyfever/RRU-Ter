from pyngrok import ngrok
import os
import time

AUTHTOKEN = os.environ.get("NGROK_AUTHTOKEN")

if not AUTHTOKEN:
    print("NGROK_AUTHTOKEN not found in environment.")
    print("To make the dashboard public, sign up at https://ngrok.com, get your authtoken,")
    print("then either run `ngrok authtoken <your-token>` or set the environment variable:")
    print("  export NGROK_AUTHTOKEN=your_token_here")
    print("After that re-run this script to create a public tunnel.")
    raise SystemExit(1)

ngrok.set_auth_token(AUTHTOKEN)

print("Starting ngrok tunnel on port 8501...")
tunnel = ngrok.connect(8501, "http")
print("NGROK_TUNNEL:", tunnel.public_url)
print("Press Ctrl+C to exit and close the tunnel.")
try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    ngrok.disconnect(tunnel.public_url)
    ngrok.kill()
