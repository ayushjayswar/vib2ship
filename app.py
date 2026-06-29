from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    tasks = data.get("tasks", "").strip().split("\n")
    
    result = "📋 Task Priority Analysis:\n\n"
    
    high_keywords = ["today", "urgent", "asap", "now", "deadline today"]
    medium_keywords = ["tomorrow", "soon", "2 days", "this week"]
    
    for i, task in enumerate(tasks):
        if not task.strip():
            continue
        task_lower = task.lower()
        
        if any(word in task_lower for word in high_keywords):
            priority = "🔴 HIGH"
            time_est = "1-2 hours"
            suggestion = "Do this immediately, don't delay!"
        elif any(word in task_lower for word in medium_keywords):
            priority = "🟡 MEDIUM"
            time_est = "2-4 hours"
            suggestion = "Plan and start today to avoid last minute rush."
        else:
            priority = "🟢 LOW"
            time_est = "Flexible"
            suggestion = "Schedule this for later in the week."
        
        result += f"Task: {task.strip()}\n"
        result += f"Priority: {priority}\n"
        result += f"Time: {time_est}\n"
        result += f"Suggestion: {suggestion}\n"
        result += "-" * 40 + "\n\n"
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)