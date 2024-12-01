# Task 8 by Nikita Verhovod

## Task a
Task a was developed with Method 2. Main/Subroutine with stepwise refinement (also Shared Data)

## Task b
Task b was developed with Method 1. Abstract Data Types

## Run Locally

Run bin file of task a from root
```bash
    ./task-a/target/build/install/task-a/bin/task-a
```

Example of result with input "Advanced software architecture task-8 task-a":
```
0000:NikitaVerhovod nsverhovod$     ./task-a/target/build/install/task-a/bin/task-a
KWIC Index:
Advanced software architecture task-8 task-a
architecture task-8 task-a Advanced software
software architecture task-8 task-a Advanced
task-8 task-a Advanced software architecture
task-a Advanced software architecture task-8
```

if you need to change input, find resources/input.txt, change text here. 
After you need to gradle installDir again and copy this build to target folder.

Run bin file of task b from root
```bash
    ./task-b/target/build/install/task-b/bin/task-b
```
Example of result:
```
 0000:NikitaVerhovod nsverhovod$ ./task-b/target/build/install/task-b/bin/task-b
 Board Configuration:
 Q . . . . . . . 
 . . . . Q . . . 
 . . . . . . . Q 
 . . . . . Q . . 
 . . Q . . . . . 
 . . . . . . Q . 
 . Q . . . . . . 
 . . . Q . . . . 

```

Or copy this project in intellij idea and do gradle run (build + assemble)

## Comparing a

| Criterion                       | Main/Subroutine (Stepwise Refinement) | Pipes-and-Filters      | Implicit Invocation (Event-Driven) |
|---------------------------------|---------------------------------------|------------------------|------------------------------------|
| Change implementation algorithm | Difficult                             | Easy                   | Normal                             |
| Change data representation      | Difficult                             | Easy                   | Normal                             |
| Add additional functions        | Normal                                | Easy                   | Easy                               |
| Performance                     | High                                  | Normal                 | Normal                             |
| Reusability                     | Normal                                | High                   | High                               |

### Explanation of Comparison

1. Change Implementation Algorithm
    - Main/Subroutine (Stepwise Refinement): This approach typically involves a sequential process, where changing the algorithm within one step may require extensive changes to the order or dependencies in the other steps. This lack of modularity makes changing the algorithm in each module difficult.
    - Pipes-and-Filters: This method is modular, with each filter functioning independently. Changing the algorithm within a filter is usually straightforward, as long as the input/output interface remains consistent. This design makes it easier to change algorithms.
    - Implicit Invocation (Event-Driven): While event-driven methods are moderately flexible, changing algorithms within modules is easier than in Main/Subroutine but may involve updating several event listeners or triggers, depending on the event handling structure.

2. Change Data Representation
    - Main/Subroutine (Stepwise Refinement): Data is often shared across subroutines or passed around, meaning a change in data representation might necessitate changes in many interconnected routines, making it difficult to adapt.
    - Pipes-and-Filters: Since each filter is independent, changing data representation within a filter is easy. Only the specific filter handling that data needs to be updated, provided the data format passed between filters remains compatible.
    - Implicit Invocation (Event-Driven): Changing data representation in event-driven approaches requires adjusting each module that consumes the data, which can be moderate in effort. However, event listeners are loosely coupled, so each can be modified independently.

3. Add Additional Functions
    - Main/Subroutine (Stepwise Refinement): Adding functions is possible but can be moderately challenging if it requires integrating the new function into the established sequence of subroutine calls. Additional adjustments may be necessary to maintain the logical flow.
    - Pipes-and-Filters: Adding functions is easy since it generally involves creating a new filter or updating an existing filter. New filters can be added with minimal impact on other parts of the pipeline, as long as they handle the required input/output format.
    - Implicit Invocation (Event-Driven): Event-driven designs allow for adding new functions easily, by introducing new event listeners or triggers. Functions are independent, so additional event-driven modules can be added without affecting existing ones.

4. Performance
    - Main/Subroutine (Stepwise Refinement): This approach is often the most performant, as control flow is tightly managed, and there’s minimal overhead.
      Data flows directly between subroutines in a predictable order, reducing latency.
    - Pipes-and-Filters: Modular but may incur some performance overhead due to the data being passed through filters. This approach has moderate performance due to the separation of concerns and the pipeline data passing overhead.
    - Implicit Invocation (Event-Driven): Event-driven architectures can introduce additional latency due to indirect communication (e.g., waiting for event responses). Thus, while flexible, they may perform slower than a strictly sequential main/subroutine design.

5. Reusability
    - Main/Subroutine (Stepwise Refinement): While some routines may be reusable, they often depend heavily on the specific sequence of operations. Reusability is moderate as reusing routines might require refactoring to fit different sequences or contexts.
    - Pipes-and-Filters: Each filter is self-contained, making it highly reusable across different pipelines or programs. Filters can often be repurposed in other contexts without modification.
    - Implicit Invocation (Event-Driven): Event-driven modules are also highly reusable. Modules designed to respond to specific events are generally easy to reuse in other event-driven systems.

### Summary
In this comparison:
   - Pipes-and-Filters and Implicit Invocation (Event-Driven) methods excel in modularity and flexibility. They make it easier to change algorithms, modify data representation, and add new functions. However, both come with moderate performance due to the modular, often loosely-coupled structure.
   - Main/Subroutine (Stepwise Refinement) offers higher performance and a straightforward sequence of operations but lacks flexibility in modifying algorithms or data representation due to its tightly coupled design.

For implementing a similar program, I would likely reuse the Pipes-and-Filters approach. This method provides a good balance of modularity and flexibility while keeping the architecture relatively simple and adaptable for future changes.


## Comparing b

| Criterion                       | Abstract Data Types (ADT) | Main/Subroutine (Stepwise Refinement) | Pipes-and-Filters     |
|---------------------------------|---------------------------|---------------------------------------|-----------------------|
| Change implementation algorithm | Normal                    | Difficult                             | Easy                  |
| Change data representation      | Normal                    | Difficult                             | Easy                  |
| Add additional functions        | Normal                    | Normal                                | Easy                  |
| Performance                     | High                      | Normal                                | Low                   |
| Reusability                     | High                      | Normal                                | Normal                |

### Explanation of Comparison

1. Change Implementation Algorithm
    - Main/Subroutine (Stepwise Refinement): This approach often involves a tightly coupled sequence of steps, so changing the implementation algorithm in any part of the program may require adjustments in multiple interconnected subroutines. This dependency makes changes challenging.
    - Pipes-and-Filters: In this approach, each filter functions independently, allowing the implementation algorithm within each filter to be modified without affecting others, as long as the data flowing between them adheres to a defined interface. This modularity makes it easy to change algorithms.
    - Implicit Invocation (Event-Driven): In an event-driven approach, the changeability depends on the specific event handlers. Modifying algorithms is moderately easy, as each module reacts to events and is typically loosely coupled. However, changes to event triggers or responses may ripple through event listeners.

2. Change Data Representation
    - Main/Subroutine (Stepwise Refinement): Shared data may be used across various subroutines, making it challenging to modify the data structure without needing to adjust each subroutine that interacts with it.
    - Pipes-and-Filters: Each filter is self-contained, and as long as the interface requirements are met, the data representation within each filter can be changed independently. This modularity makes it easy to adjust data representation.
    - Implicit Invocation (Event-Driven): Changing data representation in event-driven architectures requires updating the data used by each event listener. While this may involve multiple modules, the impact is usually localized to specific event handlers, making it moderately easy.

3. Add Additional Functions
    - Main/Subroutine (Stepwise Refinement): Adding new functions is possible, but it may require restructuring the program flow, as the sequence of subroutine calls could be impacted by the additional functionality.
    - Pipes-and-Filters: This architecture is very flexible for adding new functions by creating additional filters or modifying existing ones. New filters can be introduced with minimal impact on existing ones, provided they adhere to the data flow requirements.
    - Implicit Invocation (Event-Driven): Event-driven architectures are also highly flexible, as new functions can be added by creating new event listeners or triggers. This approach is typically easy to expand since functions can be introduced as independent modules that respond to specific events.

4. Performance
    - Main/Subroutine (Stepwise Refinement): Performance is generally high because the data flow and control are tightly controlled in a linear sequence, minimizing overhead and making it straightforward to optimize.
    - Pipes-and-Filters: While modular, the pipes-and-filters method may have performance overhead due to data transfer between filters, which can reduce performance in comparison to the tightly integrated subroutine approach.
    - Implicit Invocation (Event-Driven): Event-driven architectures can introduce latency because of the indirect communication between modules via events. While still performant, this approach generally has more overhead than a strict main/subroutine structure.

5. Reusability
    - Main/Subroutine (Stepwise Refinement): The tightly coupled nature of main/subroutine structures makes them moderately reusable but often requires significant adaptation to fit new contexts.
    - Pipes-and-Filters: Each filter operates independently, making it highly reusable in other pipelines or applications with similar data flows. Filters can often be adapted or combined with other filters for new applications.
    - Implicit Invocation (Event-Driven): Event-driven modules are highly reusable, as they are decoupled and respond to events independently. New programs can reuse event listeners or triggers with minimal adjustments.

### Summary
From this comparison, the Pipes-and-Filters and Implicit Invocation (Event-Driven) methods stand out for their flexibility and modularity, with Pipes-and-Filters being easier to change and add functionality while Implicit Invocation offers a similarly modular structure suited to event-based applications. However, Main/Subroutine (Stepwise Refinement) may be preferred for scenarios where high performance and a linear, predictable flow are essential.

If I were to implement a similar program, I would choose the Pipes-and-Filters approach for its balance between flexibility, ease of adding functionality, and modularity. This architecture would provide a robust framework for handling complex data flows while allowing for future expandability and easy modification of components.
