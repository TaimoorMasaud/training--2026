# training--2026
## Results 
```
python tasks.py add 'Fix login bug'
Task added: [1] Fix login bug

python tasks.py done 3 
Error: Task with id 3 not found.

python tasks.py list
[1] ✗ Fix login bug (Created: 2026-03-24T20:35:13.712841)

python tasks.py list --filter done
No tasks found.
```

## Q: Explain why you used a class here instead of just functions.
### A: I used classes so each Task bundles its data and behavior, and TaskManager keeps track of all tasks and handles persistence. This organizes state and operations together, making the code cleaner, reusable, and easier to extend.