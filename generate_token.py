import jwt
import datetime

SECRET_KEY = "your-secret-key"  # MUST match SSM value

payload = {
    "user_id": "123",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("Your JWT Token:")
print(token)
