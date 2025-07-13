from flask import jsonify
from models.user import User
from bson import ObjectId

class ReputationController:
    @staticmethod
    def update_reputation(user_id_to_update, reputation_delta):
        try:
            # Validate user_id
            if not ObjectId.is_valid(user_id_to_update):
                return jsonify({"❌ message": "ID de usuario inválido", "success": False}), 400

            user = User.find_by_id(user_id_to_update)
            if not user:
                return jsonify({"❌ message": "Usuario no encontrado", "success": False}), 404

            # Update reputation
            print(f"🆗 user reputation: {user.reputation}")
            user.reputation += reputation_delta
            user.save()

            resObj = {"message": "Reputación actualizada exitosamente",
                "success": True,
                "reputation": user.reputation,
                "user":user.to_dict()}
            print(resObj)

            return jsonify(resObj), 200
        except Exception as e:
            print(f"❌ Error al actualizar la reputación: {str(e)}")
            return jsonify({"message": "Error interno del servidor", "error": str(e), "success": False}), 500
