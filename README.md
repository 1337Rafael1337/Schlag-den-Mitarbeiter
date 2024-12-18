# Schlag den Mitarbeiter - Game Management System

Welcome to the **Schlag den Mitarbeiter** game management system! This project allows you to manage, configure, and display scores for custom games with a dynamic, interactive web interface. The project includes a Flask-based backend and HTML/JavaScript frontends for game control and scoreboard display.

---

## Features

- **Landing Page**: View all active games, create new games, or delete games.
- **Game Control**: Configure game settings, teams, and match results dynamically.
- **Scoreboard**: Display game progress, including scores and winners, in a visually engaging format.
- **Dynamic Updates**: Real-time updates for the scoreboard and progress visualization.
- **Mathematical Victory Detection**: Highlights the winning team when mathematically determined.
- **Responsive Design**: Optimized for all screen sizes.
- **Auto-Save**: Control page updates automatically as you make changes.
- **Data Persistence**: Data is stored in JSON format locally without requiring a database.

---

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: Local JSON file
- **Web Hosting**: Deployed via Waitress or IIS

---

## Setup and Installation

### Requirements
- Python 3.7 or later
- Flask
- Waitress (for production deployment)
- A browser for frontend interaction

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/schlag-den-mitarbeiter.git
    cd schlag-den-mitarbeiter
    ```

2. Install dependencies:
    ```bash
    pip install flask waitress
    ```

3. Start the Flask server:
    ```bash
    waitress-serve --host=0.0.0.0 --port=5000 server:app
    ```

4. Access the web interface at:
    ```
    http://<your-server-ip>:5000
    ```

---
---

## Usage Instructions

### Landing Page (`index.html`)

- **Create a Game**: Click on "Create New Game" and enter a name to initialize a new game.
- **Manage Games**:
    - Access the **Control Page** to configure game settings.
    - Access the **Scoreboard** to view real-time scores and progress.
- **Delete Games**: Remove a game from the list.

### Control Page (`control.html`)

- **Configure Teams**: Enter names for `Team 1` and `Team 2`.
- **Set Number of Matches**: Adjust the total number of matches.
- **Declare Winners**: Update winners for each match dynamically.
- **Auto-Save**: Changes are saved automatically as you make edits.

### Scoreboard Page (`scoreboard.html`)

- **Real-Time Updates**: Displays scores, percentages, and match progress dynamically.
- **Highlight Winner**: The leading team’s progress bar turns green upon mathematical victory.
- **Round-by-Round Tiles**: View individual match results with color-coded tiles:
    - Blue (`T1`) for Team 1 wins.
    - Orange (`T2`) for Team 2 wins.
    - Grey for unplayed matches.

---

## Deployment on IIS

1. Configure **Flask App** behind IIS as a FastCGI Application:
    - Use **Waitress** as the WSGI server.
    - Create a site binding on IIS pointing to your Flask app.
    - Forward requests to `localhost:5000`.

2. Setup Firewall Rules:
    - Open port `5000` to allow communication with the Flask backend.

---

## Data Persistence

- The application uses a `games.json` file to store all active game data:
    - Games
    - Teams
    - Scores
    - Match results
- The file is updated dynamically whenever changes are made in the control or scoreboard pages.

---

## Future Enhancements

- Add support for multiplayer over WebSockets.
- Implement user authentication for better game management.
- Extend support for additional game types or custom rules.

---

## Contributing

We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request. Make sure to follow the code style and document your changes.

---


## Contact

For questions or support, reach out to **Rafael Seel** at [contact@www.schlag-den-mitarbeiter.de].
