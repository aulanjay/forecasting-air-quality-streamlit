import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# --- Generate Hash Untuk Password
names = ["Admin"]
usernames = ["admin"]
passwords = ["XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

# --- Hash Password Disimpan di file hashed_pw.pkl
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file: 
    pickle.dump(hashed_passwords, file)