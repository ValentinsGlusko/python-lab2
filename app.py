from flask import Flask, request

local_db = []
current_id = 1

app = Flask(__name__)

@app.get("/")
def home_page():
    return "This is home page"

@app.post("/users")
def post_users():
    global current_id

    user = request.get_json()

    if not user or "name" not in user:
        return {"error": "Name is required"}, 400
    user = {
        "id": current_id,
        "name": user.get("name", "")
    }

    current_id += 1
    local_db.append(user)

    return {
        "message": "User created successfully",
        "user": user
    }, 201

@app.get("/users")
def get_all_users():
    return {
        "users": local_db
    }


if __name__ == "__main__":
    app.run(debug=True)