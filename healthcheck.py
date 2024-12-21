from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Version information
APP_VERSION = "1.0.0"
BUILD_DATE = "2024-12-21"

# Health check for the app and third-party services
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        # Application-specific checks
        app_status = {"status": "UP"}

        # Third-party service health checks (example: CoinGecko API)
        coingecko_url = "https://api.coingecko.com/api/v3/ping"
        coingecko_status = "DOWN"
        try:
            response = requests.get(coingecko_url, timeout=5)
            if response.status_code == 200:
                coingecko_status = "UP"
        except Exception as e:
            coingecko_status = f"ERROR: {str(e)}"

        # Combine results
        health_status = {
            "application": app_status,
            "third_party_services": {
                "coingecko_api": coingecko_status
            }
        }

        return jsonify(health_status), 200

    except Exception as e:
        # In case of unexpected errors
        return jsonify({"status": "DOWN", "error": str(e)}), 500


# Version information endpoint
@app.route('/version', methods=['GET'])
def version():
    version_info = {
        "app_version": APP_VERSION,
        "build_date": BUILD_DATE,
        "third_party_dependencies": {
            "CoinGecko API": "https://www.coingecko.com/api/documentation"
        }
    }
    return jsonify(version_info), 200


if __name__ == '__main__':
    app.run(debug=True)
