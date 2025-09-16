from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is missing. Check your .env file.")


print("Supabase URL and Key loaded successfully.")
print(f"SUPABASE_URL: {url}")
print(f"SUPABASE_KEY: {key[:4]}...{key[-4:]}")  # Print only the first and last 4 characters for security

supabase: Client = create_client(url, key)

def verify_product_key(email, product_key):
    response = supabase.table("users").select("*").execute()
    print(response.data)
#     return response.data

verify_product_key("jkhkas", "jkhkas")
