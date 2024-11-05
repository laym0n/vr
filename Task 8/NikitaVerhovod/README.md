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