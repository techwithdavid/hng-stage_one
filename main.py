from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

app.route('/api', methods=['GET'])
def details():
    slack_name = requests.args.get('slack_name')
    track = requests.args.get('track')
    current_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = datetime.datetime.now().strftime("%A")

    return jsonify({
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_time,
        'track': track,
        'github_file_url': "https://github.com/techwithdavid/h    ng-stage_one/blob/master/main.py",
        'github_repo_url': "https://github.com/techwithdavid/h    ng-stage_one",
        'status_code': 200:
        }), 200

if __name__=='__main__':
    app.run(debug=True)
    