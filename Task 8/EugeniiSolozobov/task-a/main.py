from typing import List, Callable


# Observer or listing events.
class Listener:
    def update(self, event_data):
        raise NotImplementedError("Listener must implement `update` method")


# General class of producing events
class Producer:
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_listeners(self, event_data):
        for listener in self.listeners:
            listener.update(event_data)

    # Events generator
    def produce(self, line: str):
        self.notify_listeners(line)


# KWIC problem solver
class KWICProcessor(Listener):
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    def update(self, line: str):
        if self.keyword in line.lower():
            print(f"Context for keyword '{self.keyword}': {line}")


# Main code
def main(lines: List[str], keyword: str):
    producer = Producer()
    kwic_processor = KWICProcessor(keyword)

    # Register KWICProcessor such as producer
    producer.register_listener(kwic_processor)

    # Iter each row in lines and produce new event
    for line in lines:
        producer.produce(line)


# Example
lines = [
    "Example for KWIC system for HSE subject.",
    "The HSE subject teach us to know KWIC system is event-driven and asynchronous.",
    "It highlights keywords in context for better readability.",
]
keyword = "KWIC"
main(lines, keyword)
