from flask import Blueprint, request, jsonify
from app import db
from app.models.response import Response
import logging
import random

responses_bp = Blueprint('responses_bp', __name__)

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

@responses_bp.route('/responses', methods=['POST'])
def create_response():
    data = request.get_json()
    if not data:
        logging.error("Invalid input: No data provided")
        return jsonify({"error": "Invalid input"}), 400

    required_fields = ['question_id', 'user_name', 'text']
    for field in required_fields:
        if field not in data:
            logging.error(f"Missing required field: {field}")
            return jsonify({"error": f"Missing required field: {field}"}), 400

    user_id = data.get('user_id')
    if not user_id:
        # Проверить, существует ли пользователь с таким user_name
        existing_user_name = db.session.query(Response).filter_by(user_name=data['user_name']).first()
        if existing_user_name:
            user_id = existing_user_name.user_id
        else:
            # Сгенерировать новый user_id
            user_id = random.randint(1, 1000000)
    else:
        # Проверить, существует ли пользователь с таким user_id
        existing_user = db.session.query(Response).filter_by(user_id=user_id).first()
        if not existing_user:
            # Создать нового пользователя с этим user_id
            user_id = random.randint(1, 1000000)

    try:
        response = Response(
            question_id=data['question_id'],
            user_id=user_id,
            user_name=data['user_name'],
            text=data['text']
        )
        db.session.add(response)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(f"Database error: {str(e)}")
        return jsonify({"error": str(e)}), 500

    return jsonify(response.to_dict()), 201

@responses_bp.route('/responses', methods=['GET'])
def get_responses():
    try:
        responses = Response.query.all()
        return jsonify([response.to_dict() for response in responses]), 200
    except Exception as e:
        logging.error(f"Database error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@responses_bp.route('/responses/<int:id>', methods=['DELETE'])
def delete_response(id):
    response = Response.query.get_or_404(id)
    try:
        db.session.delete(response)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(f"Database error: {str(e)}")
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Response deleted"}), 200

@responses_bp.route('/responses/<int:id>', methods=['PUT'])
def update_response(id):
    data = request.get_json()
    if not data:
        logging.error("Invalid input: No data provided")
        return jsonify({"error": "Invalid input"}), 400

    response = Response.query.get_or_404(id)
    try:
        if 'question_id' in data:
            response.question_id = data['question_id']
        if 'user_name' in data:
            response.user_name = data['user_name']
        if 'text' in data:
            response.text = data['text']
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(f"Database error: {str(e)}")
        return jsonify({"error": str(e)}), 500

    return jsonify(response.to_dict()), 200