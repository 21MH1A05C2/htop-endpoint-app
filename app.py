from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Reddy Santhu"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")

   
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {server_time}
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5000, debug=True)
