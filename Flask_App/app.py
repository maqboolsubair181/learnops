from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "CI/CD Automation Pipeline",
        "description": "End-to-end CI/CD using Jenkins, Docker, Kubernetes, ArgoCD.",
        "tech": "Jenkins, Docker, K8s, ArgoCD"
    },
    {
        "title": "AWS EKS Microservices",
        "description": "Production-grade Kubernetes cluster on AWS using Terraform.",
        "tech": "AWS, Terraform, Helm"
    },
    {
        "title": "Bitcoin Price Prediction",
        "description": "ML-based prediction system with Flask UI.",
        "tech": "Python, Flask, ML"
    }
]

@app.route("/")
def home():
    print("HOME ROUTE HIT")
    return render_template("index.html")

@app.route("/projects")
def project_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
