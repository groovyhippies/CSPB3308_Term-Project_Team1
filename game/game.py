from flask import Flask, render_template, abort
import json

app = Flask(__name__)

# Load story.json once at startup
with open('story.json') as f:
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
