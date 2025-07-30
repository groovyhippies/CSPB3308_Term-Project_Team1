from flask import Flask, render_template, abort
import json
import psycopg
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

base_dir = os.path.dirname(__file__)
story_path = os.path.join(base_dir, 'story.json')

# Load story.json once at startup
with open(story_path) as f:
    STORY = json.load(f)['nodes']

def get_node_by_id(node_id):
    return next((node for node in STORY if node['id'] == node_id), None)

@app.route('/')
def home():
    start_node=next((node for node in STORY if node['id'] == 'checkpoint_0'), None)
    return render_template('game.html', node=start_node)
   # return '<h1>Welcome to the Adventure Game</h1><a href="/node/checkpoint_0">Start Game</a>'

@app.route('/node/<node_id>')
def show_node(node_id):
    node = get_node_by_id(node_id)
    if not node:
        return abort(404)
    return render_template('game.html', node=node)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
