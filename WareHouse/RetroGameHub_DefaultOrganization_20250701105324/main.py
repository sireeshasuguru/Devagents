'''  
Main Flask application for Retro Arcade Games Gallery  
'''  
from flask import Flask, render_template  
from games_data import arcade_games  
app = Flask(__name__)  
@app.route('/')  
def index():  
    return render_template('index.html', games=arcade_games)  
if __name__ == '__main__':  
    app.run(debug=True)  