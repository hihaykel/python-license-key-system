import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# 1. Load Private Key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# 2. Customer details (e.g., email or machine ID)
customer_data = b"user@email.com"

# 3. Sign customer data with private key
signature = private_key.sign(
    customer_data,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# 4. Export license key string
license_key = base64.b64encode(signature).decode('utf-8')

with open("license.key", "w") as f:
    f.write(license_key)

print(f"License created for {customer_data.decode()}:\n{license_key}")