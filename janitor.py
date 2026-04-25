import sqlite3
from datetime import datetime, timedelta

def run_cleanup():
    db_name = "url_storage.db"
    # Calculate the cutoff (3 hours ago)
    cutoff_time = (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            # The heart of the logic: delete rows older than the cutoff
            cursor.execute("DELETE FROM urls WHERE created_at < ?", (cutoff_time,))
            print(f"[{datetime.now()}] Purge complete. Rows removed: {cursor.rowcount}")
            conn.commit()
    except Exception as e:
        print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    run_cleanup()