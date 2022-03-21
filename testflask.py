from flask import Flask, render_template, request, redirect

app = Flask('app')

@app.route('/')
def index():
	return "Hello from flask!"

app.run(host='0.0.0.0', port=8080)