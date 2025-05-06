from flask import Flask, render_template
from agent.thought_agent import ThoughtAgent

app = Flask(__name__)
agent = ThoughtAgent()

@app.route('/')
def home():
    thoughts = agent.get_thoughts()
    return render_template('index.html', thoughts=thoughts)

if __name__ == '__main__':
    app.run(debug=True)
