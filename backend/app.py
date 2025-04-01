from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database Configuration
# ควรใช้ Environment Variables ใน Production
# ตัวอย่าง: postgresql://username:password@host:port/database_name
db_user = os.environ.get('DB_USER', 'postgres') # ใส่ Username ของคุณ หรือตั้งค่าใน Env Var
db_password = os.environ.get('DB_PASSWORD', 'your_password') # ใส่ Password ของคุณ หรือตั้งค่าใน Env Var
db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'promotions_db') # ตั้งชื่อ Database ของคุณ
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Promotion Model
class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    platform = db.Column(db.String(50), nullable=False) # เช่น 'Shopee', 'Lazada'
    original_price = db.Column(db.Float, nullable=True)
    discounted_price = db.Column(db.Float, nullable=True)
    discount_percentage = db.Column(db.Float, nullable=True)
    discount_description = db.Column(db.String(255), nullable=True) # เช่น '10%', 'Buy 1 Get 1'
    url = db.Column(db.Text, nullable=False) # ลิงก์ไปยังสินค้า/โปรโมชั่นต้นทาง
    affiliate_url = db.Column(db.Text, nullable=True) # ลิงก์ Affiliate ที่สร้างขึ้น
    image_url = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    category = db.Column(db.String(100), nullable=True)
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Promotion {self.name} ({self.platform})>'

# สร้างตารางในฐานข้อมูล (ถ้ายังไม่มี)
# ควรทำผ่าน Flask-Migrate ในโปรเจกต์จริง
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Promotion Aggregator Backend!'})

# Placeholder for fetching promotions - Now from DB
@app.route('/api/promotions')
def get_promotions():
    try:
        promotions_list = Promotion.query.order_by(Promotion.last_updated.desc()).limit(50).all()
        # Convert promotion objects to dictionary format for JSON serialization
        output = []
        for promo in promotions_list:
            output.append({
                'id': promo.id,
                'name': promo.name,
                'description': promo.description,
                'platform': promo.platform,
                'original_price': promo.original_price,
                'discounted_price': promo.discounted_price,
                'discount_percentage': promo.discount_percentage,
                'discount_description': promo.discount_description,
                'url': promo.url,
                'affiliate_url': promo.affiliate_url,
                'image_url': promo.image_url,
                'start_date': promo.start_date.isoformat() if promo.start_date else None,
                'end_date': promo.end_date.isoformat() if promo.end_date else None,
                'category': promo.category,
                'last_updated': promo.last_updated.isoformat() if promo.last_updated else None
            })
        return jsonify(output)
    except Exception as e:
        # Log the error in a real application
        print(f"Error fetching promotions: {e}")
        return jsonify({"error": "Could not fetch promotions"}), 500

if __name__ == '__main__':
    app.run(debug=True) # debug=True is for development only 