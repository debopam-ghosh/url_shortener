import sqlite3
import random
import string
from datetime import datetime

class URLShortener:
    def __init__(self, db_name="url_storage.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            # created_at stores the time the link was made
            conn.execute('''CREATE TABLE IF NOT EXISTS urls
                            (short_code TEXT PRIMARY KEY, 
                             long_url TEXT, 
                             created_at TIMESTAMP)''')

    def generate_code(self):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(6))

    def shorten(self, long_url):
        code = self.generate_code()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with sqlite3.connect(self.db_name) as conn:
            try:
                conn.execute("INSERT INTO urls VALUES (?, ?, ?)", 
                             (code, long_url, current_time))
                return code
            except sqlite3.IntegrityError:
                return self.shorten(long_url) # Retry if code exists

    def get_link(self, code):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT long_url FROM urls WHERE short_code = ?", (code,))
            result = cursor.fetchone()
            return result[0] if result else "Link not found or expired."

# --- Quick Test ---
if __name__ == "__main__":
    ui = URLShortener()
    my_code = ui.shorten("https://www.tcs.com")
    print(f"Shortened Code: {my_code}")
    print(f"Retrieved URL: {ui.get_link(my_code)}")