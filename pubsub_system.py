class PubSubSystem:
    def __init__(self):
        self.topics = {}
        self.unique_subscribers = set()

    def subscribe(self, topic_id, subscriber_id, subscriber_email):
        if topic_id not in self.topics:
            self.topics[topic_id] = {}
        self.topics[topic_id][subscriber_id] = subscriber_email
        self.unique_subscribers.add(subscriber_id)
        return f"Subscriber {subscriber_id} subscribed to topic {topic_id}."

    def notify(self, topic_id):
        if topic_id not in self.topics or not self.topics[topic_id]:
            return f"No subscribers to notify for topic {topic_id}."
        
        notifications = []
        for subscriber_id, email in self.topics[topic_id].items():
            notifications.append(f"Notifying subscriber {subscriber_id} ({email}) about topic {topic_id}.")
        return notifications

    def unsubscribe(self, topic_id, subscriber_id):
        if topic_id in self.topics and subscriber_id in self.topics[topic_id]:
            del self.topics[topic_id][subscriber_id]
            if not self.topics[topic_id]:
                del self.topics[topic_id]
            self.unique_subscribers.discard(subscriber_id)
            return f"Subscriber {subscriber_id} unsubscribed from topic {topic_id}."
        else:
            return f"Subscriber {subscriber_id} is not subscribed to topic {topic_id}."

    def total_unique_subscribers(self):
        return len(self.unique_subscribers)
    
    def get_subscribers(self, topic_id):
        return self.topics.get(topic_id, {})
