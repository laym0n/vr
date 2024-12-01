
# Task 8 by Victor Kochnev

## Task a
Task a was developed with Pipes-and-filters method

## Task b
Task b was developed with Main/Subroutine with stepwise refinement

## Run Locally

Run task a
```bash
  java -jar ./task-a/target/task-a-1.0.0.jar
```
input example
```
Pattern-Oriented Software Architecture
Software Architecture
Introducing Design Patterns


```

Run task b
```bash
  java -jar ./task-b/target/task-b-1.0.0.jar
```
## Comparing

| Criterion                       | Main/Subroutine (Stepwise Refinement) | Pipes-and-Filters      | Implicit Invocation (Event-Driven) |
|---------------------------------|---------------------------------------|------------------------|------------------------------------|
| Change implementation algorithm | Difficult                             | Easy                   | Easy                               |
| Change data representation      | Normal                                | Easy                   | Easy                               |
| Add additional functions        | Normal                                | Easy                   | Easy                               |
| Performance                     | High                                  | Normal                 | Normal                             |
| Reusability                     | Difficult                             | Easy                   | Normal                             |

## Explain
1. Change Implementation Algorithm
Main/Subroutine (Stepwise Refinement): "Difficult" — This approach tightly couples steps in a single sequence, making it hard to swap or modify the algorithm without impacting the entire process.
Pipes-and-Filters: "Easy" — Filters are modular, allowing independent changes in specific stages without disrupting the entire workflow.
Implicit Invocation (Event-Driven): "Easy" — Since components are loosely connected by events, swapping out the handling algorithm is straightforwar.
2. Change Data Representation
Main/Subroutine (Stepwise Refinement): "Normal" — Data structures are typically shared across subroutines, so changing data representation may require minor adjustments but is feasible.
Pipes-and-Filters: "Easy" — Each filter is isolated, often only needing updates within a specific filter when data changes.
Implicit Invocation (Event-Driven): "Easy" — Components handle events independently, allowing each component to adjust to new data representations without major system-wide changes.
3. Add Additional Functions
Main/Subroutine (Stepwise Refinement): "Normal" — New functions can be added, but due to the tightly bound structure, it requires careful integration.
Pipes-and-Filters: "Easy" — New filters can be added to the pipeline without impacting existing filters, making it straightforward to extend functionality.
Implicit Invocation (Event-Driven): "Easy" — New event handlers or listeners can be introduced easily, provided they align with the event-based system.
4. Performance
Main/Subroutine (Stepwise Refinement): "High" — This approach typically has high performance due to fewer abstractions, direct function calls, and less communication overhead.
Pipes-and-Filters: "Normal" — While efficient, performance can be impacted by data transfers between filters.
Implicit Invocation (Event-Driven): "Normal" — Event-driven systems can incur some latency due to the use of messaging or event-passing.
5. Reusability
Main/Subroutine (Stepwise Refinement): "Difficult" — Components are typically purpose-built for the main sequence, which limits flexibility and reuse in other systems.
Pipes-and-Filters: "Easy" — Filters can often be repurposed in different pipelines or contexts due to their modular nature.
Implicit Invocation (Event-Driven): "Normal" — Event handlers are somewhat reusable, but their utility depends on matching event systems in other projects.
