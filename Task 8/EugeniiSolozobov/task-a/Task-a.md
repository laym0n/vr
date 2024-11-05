### Explanation of the Solution

To implement the Key Word in Context (KWIC) task using **Method 4. Implicit Invocation (event-driven)**, use the **Observer/Listener design pattern**. In Python, this pattern can be easily implemented with built-in methods and classes.

Below is the general structure of the KWIC solution using an observer:

- **Producer** - generates lines of text.
- **KWIC Processor** - tracks keywords in the text and highlights them in context.
- **Listener** - subscribes to events from the Producer and processes the received data.

In this way, we've implemented a **Implicit Invocation (event-driven)** architecture, aligning with the method's requirements.

Example of result:
```
Context for keyword 'kwic': Example for KWIC system for HSE subject.
Context for keyword 'kwic': The HSE subject teach us to know KWIC system is event-driven and asynchronous.
```
