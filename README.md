# Publisher-Subscriber Notification System

This is a simple Publisher-Subscriber Notification System implemented using Flask. Users can subscribe and unsubscribe to various blog topics, and receive notifications when they subscribe.

## Features

- **Subscribe to Blog Topics:** Users can subscribe to different blog topics.
- **Unsubscribe from Blog Topics:** Users can unsubscribe from the blog topics they have subscribed to.
- **Notify Subscribers:** Notify all subscribers of a particular blog topic.
- **View Subscribers:** View the list of subscribers for each blog topic.
- **Count Unique Subscribers:** Display the total number of unique subscribers.

## Blogs

Here are the blogs you can subscribe to:
- [Inpainting and Outpainting with Diffusers](https://machinelearningmastery.com/inpainting-and-outpainting-with-diffusers/)
- [5 Free Platforms to Collaborate on Machine Learning Projects](https://machinelearningmastery.com/5-free-platforms-to-collaborate-on-machine-learning-projects/)
- [Further Stable Diffusion Pipeline with Diffusers](https://machinelearningmastery.com/further-stable-diffusion-pipeline-with-diffusers/)
- [5 Useful Loss Functions](https://machinelearningmastery.com/5-useful-loss-functions/)
- [Running Stable Diffusion with Python](https://machinelearningmastery.com/running-stable-diffusion-with-python/)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yashkadam435/publisher-subscriber-system.git
cd publisher-subscriber-system
```
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
3. Install the required packages:

```bash
pip install -r requirements.txt
```
4. Run the Flask application:

```bash
python app.py
```
Open your browser and navigate to http://127.0.0.1:5000/ to view the application.

```bash
publisher-subscriber-system/
├── templates/
│   ├── index.html
│   ├── blog.html
│   ├── subscribers.html
├── app.py
├── pubsub_system.py
├── requirements.txt
├── README.md
```

1) templates/: Contains the HTML templates for the application.
2) index.html: Home page displaying the list of blogs.
3) blog.html: Blog page for subscribing and unsubscribing to a blog topic.
4) subscribers.html: Page displaying the total number of unique subscribers and any messages.
5) app.py: Main Flask application file.
6) pubsub_system.py: Contains the PubSubSystem class for managing subscriptions and notifications.
7) requirements.txt: Lists the required Python packages.
8) README.md: This file.
   
## Usage

## Home Page
Visit the home page to see a list of available blogs. Click on a blog title to view more details and subscribe or unsubscribe to the blog.
<img width="959" alt="image" src="https://github.com/yashkadam435/Publisher-Subscriber-System/assets/108817280/4d37c284-dfc7-47c8-8d19-355a4c6e0da5">

## Subscribe
1) Enter your ID and email in the subscription form on the blog page.
2) Click the "Subscribe" button.

<img width="959" alt="image" src="https://github.com/yashkadam435/Publisher-Subscriber-System/assets/108817280/060c4fdd-32fe-4b58-9f31-c1c4e35c2fa6">
<img width="959" alt="image" src="https://github.com/yashkadam435/Publisher-Subscriber-System/assets/108817280/86b6b4c5-c356-484b-8bae-fabc14691e01">

## Unsubscribe
1) Enter your ID in the unsubscribe form on the blog page.
2) Click the "Unsubscribe" button.
<img width="958" alt="image" src="https://github.com/yashkadam435/Publisher-Subscriber-System/assets/108817280/88023043-a58e-47fe-9610-2f06c1b36a3f">

## View Subscribers
Subscribers for each blog are listed on the respective blog page. The total number of unique subscribers can be viewed on the subscribers page.
<img width="898" alt="image" src="https://github.com/yashkadam435/Publisher-Subscriber-System/assets/108817280/7a8f2768-fd12-4cbc-818f-c06372f2d65d">


## Edge Cases Covered
1) Attempting to unsubscribe a non-existent subscriber or from a non-existent topic.
2) Handling subscriptions and unsubscriptions for the same user across different topics.

## License
This project is licensed under the MIT License
