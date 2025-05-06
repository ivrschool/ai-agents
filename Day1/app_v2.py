from flask import Flask, render_template, request
from agent.thought_agent_v2 import ThoughtAgent

app = Flask(__name__)
agent = ThoughtAgent()

@app.route('/')
def home():
    return render_template('index_v2.html')

@app.route('/today')
def today():
    thoughts = agent.get_thoughts(prompt_type="today")
    return render_template('index_v2.html', thoughts=thoughts, tab="today")

@app.route('/tomorrow')
def tomorrow():
    thoughts = agent.get_thoughts(prompt_type="tomorrow")
    return render_template('index_v2.html', thoughts=thoughts, tab="tomorrow")

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    thoughts = []
    topic = ""
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        if topic:
            thoughts = agent.get_custom_thoughts(topic)
    return render_template('index_v2.html', thoughts=thoughts, tab="custom", topic=topic)

if __name__ == '__main__':
    app.run(debug=True)