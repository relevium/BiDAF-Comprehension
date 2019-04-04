from flask import Flask, request, jsonify
import requests, time, json, logic
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'vist to /api'

@app.route('/api', methods=['GET'])
def sample():

    example = """
    {"passage": "Mohamed Salah started his senior career with Cairo club El Mokawloon in the Egyptian Premier League in 2010, departing shortly thereafter to join Basel for an undisclosed fee. In Switzerland, he starred as he won the league title in his debut season, winning the SAFP Golden Player Award in the process. Salah's performances then attracted Premier League side Chelsea, and he joined the club for a $11 million fee in 2014. However, he was used sparingly in his debut season and was allowed to leave on loan to Serie A clubs Fiorentina and Roma, with the latter eventually signing him permanently for $15 million.", "question": "what year did Mohamed Salah start his senior career?"}
    """

    return "<h1>Usage</h1>Please send me a POST JSON request with a passage and a question <h1>Example</h1>" + example


@app.route('/api', methods=['POST'])
def mc():
    query = request.get_json()
    ans = logic.comprehend(query['passage'], query['question'])
    # ans = ans.json()
    with open('logs/' + str(int(time.time())), 'w') as f:
        json.dump([query, ans["best_span_str"]], f)
    return jsonify(answer= ans["best_span_str"]), 200
