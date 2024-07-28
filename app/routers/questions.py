from flask import Blueprint, request, jsonify
from app import db
from app.models import Question, Response

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions', methods=['GET', 'POST'])
def handle_questions():
    if request.method == 'GET':
        questions_list = Question.query.all()
        return jsonify([q.to_dict() for q in questions_list]), 200
    elif request.method == 'POST':
        try:
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": f"Failed to decode JSON object: {str(e)}"}), 400

        if not data:
            return jsonify({"error": "No data provided"}), 400

        if isinstance(data, dict):
            data = [data]

        if not isinstance(data, list):
            return jsonify({"error": "Request data should be a list of questions or a single question"}), 400

        new_questions = []
        for item in data:
            if 'title' not in item or 'body' not in item:
                return jsonify({"error": "Each question must have 'title' and 'body'"}), 400
            new_question = Question()
            new_question.update(item)
            db.session.add(new_question)
            new_questions.append(new_question)
        db.session.commit()
        return jsonify([q.to_dict() for q in new_questions]), 201

@questions_bp.route('/questions/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def handle_question(id):
    question = Question.query.get(id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    if request.method == 'GET':
        return jsonify(question.to_dict()), 200

    elif request.method in ['PUT', 'PATCH']:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        question.update(data)
        db.session.commit()
        return jsonify(question.to_dict()), 200

    elif request.method == 'DELETE':
        db.session.delete(question)
        db.session.commit()
        return jsonify({"message": "Question deleted"}), 200

@questions_bp.route('/questions_with_responses', methods=['GET'])
def get_questions_with_responses():
    questions_list = Question.query.all()
    result = []
    for question in questions_list:
        question_dict = question.to_dict()
        responses = Response.query.filter_by(question_id=question.id).all()
        question_dict['responses'] = [response.to_dict() for response in responses]
        result.append(question_dict)
    return jsonify(result), 200