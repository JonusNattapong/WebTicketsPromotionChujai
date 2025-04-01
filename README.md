# Web Promotion Aggregator (ชื่อชั่วคราว)

เว็บแอปพลิเคชันสำหรับรวบรวมโปรโมชั่น ส่วนลด และดีลพิเศษต่างๆ จากแพลตฟอร์ม E-commerce และบริการออนไลน์ชั้นนำในประเทศไทย โดยมีเป้าหมายเพื่อเป็นศูนย์กลางให้ผู้ใช้ค้นหาโปรโมชั่นที่น่าสนใจได้อย่างสะดวกและรวดเร็ว พร้อมสร้างรายได้ผ่าน Affiliate Marketing

## ✨ คุณสมบัติหลัก (Features - Planned)

*   รวบรวมโปรโมชั่นจากหลายแพลตฟอร์ม (เช่น Shopee, Lazada, Agoda, Klook)
*   แสดงรายละเอียดโปรโมชั่น (ส่วนลด, ราคา, รูปภาพ, เงื่อนไข, วันหมดอายุ)
*   ระบบค้นหาและกรองโปรโมชั่นตามแพลตฟอร์ม, หมวดหมู่, หรือคำค้น
*   สร้าง Affiliate Link อัตโนมัติเมื่อผู้ใช้คลิกไปยังแพลตฟอร์มเป้าหมาย
*   หน้าจอสวยงาม ใช้งานง่าย (MUI)

## 💻 เทคโนโลยีที่ใช้ (Technology Stack)

*   **Backend:**
    *   ภาษา: Python 3.x
    *   Framework: Flask
    *   ฐานข้อมูล: PostgreSQL
    *   ORM: Flask-SQLAlchemy
    *   การจัดการฐานข้อมูล: SQLAlchemy (เบื้องต้น), Flask-Migrate (แนะนำสำหรับ Production)
    *   จัดการ Background Tasks: Celery + Redis/RabbitMQ (วางแผนไว้)
*   **Frontend:**
    *   Library: React.js
    *   UI Components: Material-UI (MUI)
    *   จัดการ State: (ยังไม่ได้กำหนด - อาจใช้ Context API หรือ Redux)
    *   Package Manager: npm
*   **การพัฒนาและ Deploy (เบื้องต้น):**
    *   Containerization: Docker (แนะนำ)
    *   Environment Variables: python-dotenv

## 🚀 ข้อกำหนดเบื้องต้น (Prerequisites)

ก่อนเริ่มต้น คุณต้องติดตั้งซอฟต์แวร์ต่อไปนี้บนเครื่องของคุณ:

*   [Python](https://www.python.org/downloads/) (เวอร์ชัน 3.8 ขึ้นไป)
*   [Node.js](https://nodejs.org/) (เวอร์ชัน 16.x ขึ้นไป แนะนำ LTS) และ npm
*   [PostgreSQL](https://www.postgresql.org/download/) (เวอร์ชัน 12 ขึ้นไป) หรือ Docker สำหรับรัน PostgreSQL Container
*   [Git](https://git-scm.com/)

## 🛠️ การติดตั้ง (Setup and Installation)

1.  **Clone Repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **ตั้งค่า Backend:**
    *   **เข้าไปที่โฟลเดอร์ Backend:**
        ```bash
        cd backend
        ```
    *   **สร้างและ Activate Virtual Environment:**
        ```bash
        # Windows
        python -m venv venv
        venv\\Scripts\\activate

        # macOS / Linux
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   **ตั้งค่าฐานข้อมูล PostgreSQL:**
        *   สร้าง Database ใน PostgreSQL (เช่น ชื่อ `promotions_db`)
        *   สร้างไฟล์ `.env` ในโฟลเดอร์ `backend` (คัดลอกจาก `.env.example` ถ้ามี หรือสร้างใหม่) และกำหนดค่าการเชื่อมต่อ:
            ```.env
            # ตัวอย่าง .env
            DB_USER=your_postgres_user
            DB_PASSWORD=your_postgres_password
            DB_HOST=localhost # หรือ IP/Host ของ DB Server
            DB_PORT=5432     # Port ของ DB Server
            DB_NAME=promotions_db # ชื่อ Database ที่สร้างไว้
            ```
        *   *หมายเหตุ:* คุณสามารถแก้ไขค่า Default ใน `app.py` โดยตรงได้ แต่ **ไม่แนะนำ** สำหรับข้อมูล sensitive
    *   **ติดตั้ง Dependencies:**
        ```bash
        pip install -r requirements.txt
        pip install python-dotenv # ถ้าใช้วิธี .env
        ```
        *ระบบจะพยายามสร้างตาราง `promotion` อัตโนมัติเมื่อรันครั้งแรกผ่าน `db.create_all()`*

3.  **ตั้งค่า Frontend:**
    *   **กลับไปที่ Root Directory และเข้าโฟลเดอร์ Frontend:**
        ```bash
        cd ../frontend
        # หรือ ถ้ายังอยู่ที่ root: cd frontend
        ```
    *   **ติดตั้ง Dependencies:**
        ```bash
        npm install
        ```

## ▶️ การรันแอปพลิเคชัน (Running the Application)

1.  **รัน Backend Server:**
    *   เปิด Terminal ใหม่ หรือใช้ Terminal เดิมที่ Activate venv ไว้
    *   ตรวจสอบว่าอยู่ในโฟลเดอร์ `backend`
    *   (ถ้ายังไม่ได้ Activate venv: `venv\Scripts\activate` หรือ `source venv/bin/activate`)
    *   รัน Flask Development Server:
        ```bash
        flask run
        ```
    *   Backend API จะทำงานที่ `http://127.0.0.1:5000` (หรือ Port อื่นที่ Flask กำหนด)

2.  **รัน Frontend Development Server:**
    *   เปิด Terminal ใหม่
    *   เข้าไปที่โฟลเดอร์ `frontend`
    *   รัน React App:
        ```bash
        npm start
        ```
    *   แอปพลิเคชัน Frontend จะเปิดใน Browser อัตโนมัติที่ `http://localhost:3000`

ตอนนี้คุณควรจะเห็นหน้าเว็บเบื้องต้น และสามารถเข้าถึง API Endpoint `/api/promotions` (ซึ่งตอนนี้จะยังไม่มีข้อมูล นอกจากจะเพิ่มเข้าไปใน DB โดยตรง)

## 🗄️ การจัดการฐานข้อมูล (Database Migrations)

ปัจจุบัน ระบบใช้ `db.create_all()` ใน `app.py` เพื่อสร้างตารางเมื่อเริ่มแอปฯ ซึ่งเหมาะสำหรับการเริ่มต้น

**สำหรับโปรเจกต์จริง แนะนำให้ใช้ Flask-Migrate:**
*   **ติดตั้ง:** `pip install Flask-Migrate`
*   **ตั้งค่า:** เพิ่มการตั้งค่า Migrate ใน `app.py`
*   **คำสั่ง:** ใช้คำสั่ง `flask db init`, `flask db migrate`, `flask db upgrade` เพื่อจัดการการเปลี่ยนแปลง Schema ของฐานข้อมูลอย่างเป็นระบบ

(TODO: เพิ่มการตั้งค่าและการใช้งาน Flask-Migrate)

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```
.
├── .git/
├── .gitignore
├── backend/             # โค้ดฝั่ง Backend (Flask API)
│   ├── venv/            # Python Virtual Environment (ไม่ควรอยู่ใน Git)
│   ├── app.py           # ไฟล์หลักของ Flask Application
│   ├── requirements.txt # Python Dependencies
│   ├── models.py        # (แนะนำ) แยก Model ออกมาไว้ที่นี่
│   ├── routes.py        # (แนะนำ) แยก Routes/Endpoints ออกมา
│   ├── services/        # (แนะนำ) แยก Business Logic / Service ต่างๆ
│   └── .env             # (แนะนำ) เก็บ Environment Variables (ไม่ควรอยู่ใน Git)
├── frontend/            # โค้ดฝั่ง Frontend (React App)
│   ├── node_modules/    # Node.js Dependencies (ไม่ควรอยู่ใน Git)
│   ├── public/          # ไฟล์ Static ต่างๆ
│   ├── src/             # โค้ด React Components และ Logic
│   │   ├── App.js       # Main App Component
│   │   ├── index.js     # Entry point
│   │   └── components/  # โฟลเดอร์สำหรับ UI Components
│   ├── package.json
│   └── package-lock.json
└── README.md            # ไฟล์ที่คุณกำลังอ่านอยู่
```

## 🔗 API Endpoints (เบื้องต้น)

*   `GET /`: ข้อความต้อนรับจาก Backend
*   `GET /api/promotions`: ดึงรายการโปรโมชั่นล่าสุด 50 รายการจากฐานข้อมูล

(TODO: เพิ่มรายละเอียด Endpoint เพิ่มเติมเมื่อมีการพัฒนา)

## 🤝 การสนับสนุน (Contributing)

(TODO: เพิ่มแนวทางการ Contribution ถ้าต้องการเปิดเป็น Open Source)

## 📄 สัญญาอนุญาต (License)

(TODO: เพิ่ม License เช่น MIT)