from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인에서 접근 가능하도록 설정

# Albion Online 서버 상태 API 주소
SERVERS = {
    "eu": "https://www.albionstatus.com/api/status/eu",
    "asia": "https://www.albionstatus.com/api/status/asia",
    "west": "https://www.albionstatus.com/api/status/us"
}

def get_server_status(server_name):
    """AlbionStatus에서 특정 서버 상태 가져오기"""
    try:
        response = requests.get(SERVERS[server_name])
        if response.status_code == 200:
            return response.json().get("status", "Unknown")
        return "API 오류"
    except Exception as e:
        return f"오류 발생: {e}"

@app.route("/status")
def status():
    """Albion 서버 상태 API"""
    return jsonify({
        "eu": get_server_status("eu"),
        "asia": get_server_status("asia"),
        "west": get_server_status("west")
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
