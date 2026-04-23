from flask import Flask, jsonify, request
from services.user_service import register_user
# استدعاء المكتبه لتشغيل السيرفر
app = Flask(__name__)

# تحديد المسار الي بشتغل عليه


@app.route('/api/register', methods=['POST'])
def api_register():
    user_data = request.get_json()  # هنا ناخذ البيانات ونحولها ل قاموس
    role = user_data.get('role', 'user')  # هنا ندع المستخدم يكون افتراضي
    try:  # استخدمة تري لكي لا ينهار البرنامج
        result = register_user(user_data, role)  # استدعينا الداله حقت التسجيل
        if result.get("is_valid"):  # هنا نتاكد بن التسجيل نجح
            return jsonify({"message": "Success!"}), 201
        else:  # هنا العكس
            return jsonify({"errors": result.get("errors")}), 400
    except Exception as e:  # في حال الخطأ كان من النظام نرسل هذا
        print(f"Error {e}")
        return jsonify({"error": "Database save failed"}), 500


# امر تشغيل السيرفر
if __name__ == "__main__":
    app.run(debug=True)
