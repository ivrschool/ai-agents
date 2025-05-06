from flask import Flask, render_template
from agent.thought_agent_v1 import ThoughtAgent

app = Flask(__name__)
agent = ThoughtAgent()

@app.route('/')
def home():
    return render_template('index_v1.html')

@app.route('/today')
def today():
    thoughts = agent.get_thoughts(prompt_type="today")
    return render_template('index_v1.html', thoughts=thoughts, tab="today")

@app.route('/tomorrow')
def tomorrow():
    thoughts = agent.get_thoughts(prompt_type="tomorrow")
    return render_template('index_v1.html', thoughts=thoughts, tab="tomorrow")

if __name__ == '__main__':
    app.run(debug=True)