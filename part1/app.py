from flask import Flask, jsonify, request
from services.user_service import register_user, login_user
from core.database import fetch_all
# استدعاء المكتبه لتشغيل السيرفر
app = Flask(__name__)
# هنا نجعل الترتيب الذي وضعنه يكون زي ماهو ولا يتغير بترتيب ابجدي
app.json.sort_keys = False
# تحديد المسار الي بشتغل عليه


@app.route('/api/register', methods=['POST'])
def api_register():  # مسار انشاء حساب جديد
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


@app.route('/api/login', methods=['POST'])
def api_login():  # مسار تسجيل الدخول
    user_data = request.get_json()
    # هنا حددنا من القاموس الي نحتاجه وهو الايميل والمغير الثاني نفسه
    user_email = user_data.get('email')
    user_pass = user_data.get('password')
    if not user_email or not user_pass:  # هنا نتاكد بانهم غير فارغين او توجد مسافات
        return jsonify({"error": "Email or password is required."}), 400
    try:
        # هنا استدعاء دالة تسجيل الدخول بعد التحقق
        success = login_user(user_email, user_pass)
        if success.get("is_valid"):  # هنا نتاكد بان البيانات صحيحه
            return jsonify({"user": success["user"]}), 200
        else:
            return jsonify({"errors": success.get("errors")}), 401
    except Exception as e:
        print(f"Error {e}")
        return jsonify({"error": "Database save failed"}), 500


@app.route('/api/places', methods=["GET"])
def get_places():  # مسار عرض الاماكن
    try:
        places = fetch_all(
            "SELECT id, title, description, price, latitude, longitude, amenity_id, user_id FROM place")

        place_data = []
        for row in places:
            place_data.append({"id": row[0], "title": row[1], "description": row[2], "price": row[3],
                               "latitude": row[4], "longitude": row[5], "amenity_id": row[6], "user_id": row[7]})
        return jsonify({"places": place_data}), 200
    except Exception as e:
        print(f"Error {e}")
        return jsonify({"error": "Database save failed"}), 500

    # امر تشغيل السيرفر
if __name__ == "__main__":
    app.run(debug=True)
