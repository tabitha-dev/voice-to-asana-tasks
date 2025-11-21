# Architecture overview

This project follows a simple but extensible pipeline from audio to Asana tasks.

1. Audio is recorded and converted to a text transcript.
2. The transcript is mapped into a CSV file with task and subtask fields.
3. The Python script reads the CSV and groups rows by task.
4. The script calls the Asana REST API to create tasks and subtasks.
5. A second CSV is written that stores the Asana IDs for all created items.

```text
Audio Recording
      |
      v
Transcript Text
      |
      v
CSV Structuring
(task_name, notes, subtasks)
      |
      v
Python Automation Script
      |
      v
Asana API
(create tasks and subtasks)
      |
      v
Output Registry CSV
(stable identifiers for future automation)
```

This separation of stages makes the workflow easier to reason about, test, and extend.
