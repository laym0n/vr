
# Task 8 by Eugenii Solozobov

## Task a
Task a: method 4. Was developed with Implicit invocation (event-driven) method.

## Task b
Task b: method 3. Was developed with Pipes-and-filters method.

## Run Locally

## Must be installed:

- Python 3

## Clone project

```
git clone https://github.com/laym0n/wr.git
```
## Create virtual enviroment

```
python 3 -m venv venv
```
## Launch venv on MacOS/Linux

```
source venv/bin/activate
```
## Launch venv on  Windows

```
venv/Scripts/activate
```

## Instal pip requirements

```
pip install -r Task8/EugeniiSolozobov/requirements.txt
```
Run task a
```bash
python Task8/EugeniiSolozobov/task-a/main.py
```

Run task b
```bash
python Task8/EugeniiSolozobov/task-b/main.py
```

Examples into code with launch and in their .md file

## Comparing solutions
Here’s a table comparing solutions to **Problems A and B** using different methods.  **Method 1: Abstract Data Types** and **Method 2: Main/Subroutine with Stepwise Refinement** while I applied **Method 3: Pipes-and-Filters** for **Problem B (Eight Queens)** and **Method 4: Implicit Invocation (Event-driven)** for **Problem A (KWIC)**.

```markdown
| Criteria                                          | Method 1: Abstract Data Types                                   | Method 2: Main/Subroutine with Stepwise Refinement               | My Solution (Problem A: Implicit Invocation, Problem B: Pipes-and-Filters)              | Explanation                                                                                                                                                             |
|---------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ease of Changing Implementation Algorithm**     | Moderate: Encapsulated modules allow for easier change in logic but require updating interfaces. | Moderate to Difficult: Main/subroutine requires careful step-by-step adjustments to prevent dependency issues. | Easy for Pipes-and-Filters: Independent filters allow quick, isolated changes in each step; Moderate for Implicit Invocation due to event dependency. | My solution is easier to adjust as each component operates independently, especially for the **Pipes-and-Filters** structure. However, event dependencies in **Implicit Invocation** add complexity. |
| **Ease of Changing Data Representation**          | Moderate to Difficult: Changing data representation requires updating all related classes and methods. | Difficult: Changes require adjustments throughout the main/subroutine structure, as data is often shared directly. | Easy: Data flows through isolated filters in **Pipes-and-Filters**; Moderate in **Implicit Invocation**, as listeners may depend on specific data formats. | **Pipes-and-Filters** supports easy changes to data format, as filters can transform data independently. **Main/Subroutine** is tightly coupled, making changes harder.                    |
| **Ease of Adding New Functions**                  | Moderate to Easy: New classes and methods can be added to encapsulate new functionality. | Moderate to Difficult: Adding functionality may require re-structuring of main and subroutines. | Easy: In **Pipes-and-Filters**, new filters can be added independently; Moderate for **Implicit Invocation**, as new events and listeners must be managed. | Adding new filters is straightforward in **Pipes-and-Filters**. **Abstract Data Types** is also modular but requires managing dependencies between classes.                         |
| **Performance**                                   | Moderate: Method 1 is performant but could have some overhead from encapsulated structures. | High: Main/Subroutine often offers efficient, direct calls but could suffer from bottlenecks in large subroutines. | Moderate: **Pipes-and-Filters** may introduce latency due to data transfer; **Implicit Invocation** can be slower with multiple event listeners. | **Main/Subroutine** tends to be performant for single-pass computations. My methods, especially **Pipes-and-Filters**, prioritize modularity over raw speed.                               |
| **Preferred Solution for Similar Programs**       | Not preferred: Would not choose if flexibility and ease of changes are important. | Not preferred: Suitable for simpler, smaller programs but less flexible for changes and expansions. | Preferred: **Pipes-and-Filters** for structured, modular tasks; **Implicit Invocation** for event-driven tasks. | **Pipes-and-Filters** is ideal for scalable, modular solutions where each component is isolated. **Implicit Invocation** works well in dynamic, event-driven applications.         |
```

### Checklist:

1. **Ease of Changing Implementation Algorithm**:
   - **Pipes-and-Filters** (my solution) allows for straightforward changes to each filter’s algorithm since each component is independent and interacts only through data pipes.
   - **Abstract Data Types** also support algorithmic changes within encapsulated modules, though this requires keeping interfaces consistent with other classes.
   - **Main/Subroutine** is more rigid, requiring careful refactoring to avoid impacting dependent steps.

2. **Easy of Changing Data Representation**:
   - **Pipes-and-Filters** supports changing data representation efficiently since filters can handle or transform the data independently.
   - **Abstract Data Types** make data changes challenging due to encapsulated structures, while **Main/Subroutine** relies heavily on shared data, requiring extensive updates when the data structure changes.

3. **Easy of Adding New Functions**:
   - **Pipes-and-Filters** is ideal for adding new functions, as new filters can be added with minimal disruption to the rest of the pipeline.
   - **Abstract Data Types** also allow new classes or methods, but dependencies between classes must be managed.
   - **Main/Subroutine** requires more careful restructuring since new functions may affect existing subroutine flow.

4. **Performance**:
   - **Main/Subroutine** often performs well with direct function calls but lacks flexibility in large or modular applications.
   - **Pipes-and-Filters** can introduce latency due to data handling and component isolation, though it is more manageable for structured modular designs.
   - **Implicit Invocation** may experience performance hits from event handling but works well in asynchronous, event-driven contexts.

5. **Preferred Solution for Similar Programs**:
   - **Pipes-and-Filters** and **Implicit Invocation** provide a balance of modularity and flexibility, making them ideal for complex, scalable applications.
   - **Main/Subroutine** is effective for simpler tasks with a clear, linear structure, but not ideal for applications requiring frequent updates or modularity.
   - **Abstract Data Types** offer a modular approach, though they require more effort to manage class interactions and dependencies.
