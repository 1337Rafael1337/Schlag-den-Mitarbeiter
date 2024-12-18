from flask import Flask, request, jsonify, send_from_directory
import os
import json
import logging
from datetime import datetime, timedelta

app = Flask(__name__)

# Logging-Konfiguration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

DATA_FILE = 'games.json'

# Überprüfen und Laden der JSON-Datei
def load_games():
    if not os.path.exists(DATA_FILE):
        logging.info(f"Datei {DATA_FILE} existiert nicht. Erstelle eine neue Datei.")
        with open(DATA_FILE, 'w') as f:
            json.dump({"games": []}, f)

    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logging.error(f"Fehler beim Lesen der Datei {DATA_FILE}. Datei wird neu initialisiert.")
            return {"games": []}

# Speichern der Spiele-Daten in der JSON-Datei
def save_games(games_data):
    with open(DATA_FILE, 'w') as f:
        json.dump(games_data, f, indent=4)
    logging.info(f"Spiele-Daten erfolgreich gespeichert in {DATA_FILE}.")

# Route für die Startseite (Landing Page)
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Route für die Konfigurationsseite des Spiels (control.html)
@app.route('/control')
def control():
    return send_from_directory('.', 'control.html')

# Route für die Punktetafel des Spiels (scoreboard.html)
@app.route('/scoreboard')
def scoreboard():
    return send_from_directory('.', 'scoreboard.html')

# Route zum Bereitstellen von statischen Dateien (z. B. Logo.png)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

# API-Routen für das Erstellen und Verwalten von Spielen
@app.route('/api/games', methods=['POST'])
def create_game():
    games_data = load_games()
    game_name = request.json.get("name")
    if not game_name:
        return jsonify({"error": "Spielname erforderlich"}), 400

    # Hinzufügen des Erstellungsdatums
    created_at = datetime.now().isoformat()

    new_game = {
        "game_id": str(len(games_data["games"]) + 1),
        "name": game_name,
        "created_at": created_at,
        "players": []
    }

    games_data["games"].append(new_game)
    save_games(games_data)
    logging.info(f"Neues Spiel erstellt: {new_game}")

    return jsonify(new_game)

# API-Routen zum Abrufen der Spiele (GET)
@app.route('/api/games', methods=['GET'])
def get_games():
    games_data = load_games()
    logging.info("Spiele-Daten abgerufen.")
    return jsonify(games_data["games"])

# Route zum Löschen eines Spiels
@app.route('/api/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    games_data = load_games()

    # Finde das Spiel mit der passenden ID und lösche es
    game_exists = False
    updated_games = []
    for game in games_data["games"]:
        if game["game_id"] == game_id:
            game_exists = True
            logging.info(f"Spiel gefunden und gelöscht: {game}")
        else:
            updated_games.append(game)

    if not game_exists:
        logging.warning(f"Spiel mit ID {game_id} nicht gefunden.")
        return jsonify({"error": "Spiel nicht gefunden"}), 404

    games_data["games"] = updated_games
    save_games(games_data)
    logging.info(f"Spiel mit ID {game_id} wurde erfolgreich gelöscht.")

    return jsonify({"message": "Spiel gelöscht"})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
