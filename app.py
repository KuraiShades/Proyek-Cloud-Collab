from flask import Flask, jsonify, request, abort
import random
from datetime import datetime

app = Flask(__name__)
SECRET_API_KEY = "rahasia_123"
ALLOWED_IPS = ["180.242.129.156","125.166.95.210","34.124.213.41"]

@app.route('/api/telemetry', methods=['GET'])
def generate_network_log():
    kunci_dari_klien = request.args.get('key')
    
    if kunci_dari_klien != SECRET_API_KEY:
        abort(401, description="Akses Ditolak:API Key tidak valid!")
    
    ip_klien = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    if ip_klien:
        ip_asli = ip_klien.split(',')[0].strip()

        if ip_asli not in ALLOWED_IPS:
            abort(403, description=f"Akses Ditolak: IP {ip_asli} tidak diizinkan masuk.")

        else:
            log_data = {
                        "timestamp": datetime.now().isoformat(),
                        "source_ip": f"192.168.1.{random.randint(2, 50)}",
                        "destination_ip": "10.0.0.1",
                        "latency_ms": round(random.uniform(5.0,150.0),2),
                        "packet_loss_percent": round(random.uniform(0.0,2.0), 2),
                        "bandwidth_usage_mbps": round(random.uniform(10.0, 100.0), 2)
                    }    
        
            if random.random()>0.8:
                log_data["latency_ms"] = round(random.uniform(300.0, 999.0), 2)
                log_data["packet_loss_percent"] = round(random.uniform(10.0, 50.0), 2)

            return jsonify(log_data)
    
    else:
        abort(404, description='Salah IP')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)