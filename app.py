from flask import Flask, render_template, request, redirect, url_for
from pubsub_system import PubSubSystem

app = Flask(__name__)
pubsub = PubSubSystem()

blogs = {
    "blog1": {"title": "Inpainting and Outpainting with Diffusers", "url": "https://machinelearningmastery.com/inpainting-and-outpainting-with-diffusers/"},
    "blog2": {"title": "5 Free Platforms to Collaborate on Machine Learning Projects", "url": "https://machinelearningmastery.com/5-free-platforms-to-collaborate-on-machine-learning-projects/"},
    "blog3": {"title": "Further Stable Diffusion Pipeline with Diffusers", "url": "https://machinelearningmastery.com/further-stable-diffusion-pipeline-with-diffusers/"},
    "blog4": {"title": "5 Useful Loss Functions", "url": "https://machinelearningmastery.com/5-useful-loss-functions/"},
    "blog5": {"title": "Running Stable Diffusion with Python", "url": "https://machinelearningmastery.com/running-stable-diffusion-with-python/"}
}

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)

@app.route('/blog/<blog_id>')
def blog(blog_id):
    blog = blogs.get(blog_id)
    subscribers = pubsub.get_subscribers(blog_id)
    return render_template('blog.html', blog=blog, blog_id=blog_id, subscribers=subscribers)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    topic_id = request.form['topic_id']
    subscriber_id = request.form['subscriber_id']
    subscriber_email = request.form['subscriber_email']
    message = pubsub.subscribe(topic_id, subscriber_id, subscriber_email)
    return redirect(url_for('subscribers', message=message))

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    topic_id = request.form['topic_id']
    subscriber_id = request.form['subscriber_id']
    message = pubsub.unsubscribe(topic_id, subscriber_id)
    return redirect(url_for('subscribers', message=message))

@app.route('/subscribers')
def subscribers():
    message = request.args.get('message')
    total_subscribers = pubsub.total_unique_subscribers()
    return render_template('subscribers.html', message=message, total_subscribers=total_subscribers)

if __name__ == "__main__":
    app.run(debug=True)
