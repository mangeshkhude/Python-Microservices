from flask import Flask, request, jsonify
from flask_restful import reqparse

app = Flask(__name__)
users_seen = {}

@app.route('/GetUserService/<limit>', methods=['POST'])
def get_user_service(limit):
   return "Limit is : %s" %limit

# http://172.16.20.87:5000/AddUserResult/
@app.route('/api/user/AddUserScore/', methods=['POST'])
def add_user_score():
    parser = reqparse.RequestParser()
    parser.add_argument('UserEmailID')
    parser.add_argument('UserToken', type=str)
    parser.add_argument('TestDuration', type=str)
    parser.add_argument('QuestionsCount', type=str)
    parser.add_argument('RewardPoints', type=str)
    parser.add_argument('TestDate', type=str)
    parser.add_argument('CorrectAnswersCount', type=str)
    parser.add_argument('InCorrectAnswersCount', type=str)
    args = parser.parse_args()
    my_dict = {
       'status': True,
       'UserEmailID': '{}'.format(args['UserEmailID']),
       'UserToken': '{}'.format(args['UserToken']),
       'TestDuration': '{}'.format(args['TestDuration']),
       'QuestionsCount': '{}'.format(args['QuestionsCount']),
       'RewardPoints': '{}'.format(args['RewardPoints']),
       'TestDate': '{}'.format(args['TestDate']),
       'CorrectAnswersCount': '{}'.format(args['CorrectAnswersCount']),
       'InCorrectAnswersCount': '{}'.format(args['InCorrectAnswersCount'])
    }
    return jsonify(my_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)