# Voice to Asana Tasks with Python

This project converts voice recordings into structured tasks and subtasks inside Asana using a simple CSV based workflow and the Asana REST API.

The goal is to reduce manual data entry and create a repeatable path from unstructured audio or meeting transcripts to actionable work in Asana.

## Features

- Converts transcript text into a structured CSV format
- Creates Asana tasks and subtasks from the CSV
- Stores stable Asana identifiers for future automation
- Designed to extend to meeting recordings, team workflows, and voice assistants

## High level workflow

1. Record audio on a phone or in a meeting tool  
2. Convert the audio into a text transcript  
3. Map the transcript into a CSV with tasks and subtasks  
4. Run the Python script to create tasks in Asana  
5. Use the generated output CSV as a registry of Asana IDs

### System overview

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

## Repository structure

```text
src/
  csv_to_asana.py      # core script that talks to the Asana API
  app.py               # optional entry point (CLI wrapper)
  config_example.py    # example configuration for tokens and IDs
data/
  samples/
    tasks_sample.csv           # sample input CSV
    tasks_with_ids_sample.csv  # sample output CSV
docs/
  architecture.md       # deeper explanation of the design
  article_linkedin.md   # long form article about the project
```

## CSV format

The script expects an input CSV similar to:

```csv
task_name,notes,subtask_name,subtask_notes
Plan holiday trip,"Overall planning and bookings","Book flights","Compare prices and book tickets"
Plan holiday trip,"Overall planning and bookings","Reserve hotel","Check options and book hotel"
Weekly cleaning,"Household tasks","",""
Pay bills,"Monthly payments","Pay electricity bill","Due next week"
```

Rules:

- task_name is required
- notes is optional
- subtask_name and subtask_notes are optional
- Multiple rows with the same task_name and notes become subtasks under one Asana parent task

The script will produce an output CSV that includes the Asana IDs created for tasks and subtasks.

## Core script

The core logic lives in `src/csv_to_asana.py`. See that file for the most up to date implementation.

## Configuration

Create a file called `config.py` in the `src` folder (do not commit your real token) and set:

```python
ASANA_TOKEN = "your_real_personal_access_token"
ASANA_PROJECT_ID = "your_project_gid"
```

Then import from it instead of hard coding:

```python
from config import ASANA_TOKEN, ASANA_PROJECT_ID
```

Add `config.py` to `.gitignore` so it is never committed.

## Installation and usage

1. Clone the repository

```bash
git clone https://github.com/yourusername/voice-to-asana-tasks.git
cd voice-to-asana-tasks
```

2. (Optional) Create and activate a virtual environment

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create your `src/config.py` with your Asana token and project ID

5. Place your input CSV into `data/samples/tasks_sample.csv`  
   or update the file path in `src/app.py`

6. Run the script

```bash
python src/app.py
```

After it runs, check Asana for new tasks and check the output CSV for the stored Asana IDs.

## Asana developer resources

- Asana Developer Platform  
  https://asana.com/developers  

- Asana REST API Reference  
  https://developers.asana.com/reference/rest-api-reference  

- Quick start guide  
  https://developers.asana.com/docs/quick-start  

- Asana App Directory  
  https://asana.com/apps  

These links are helpful if you want to extend this project into more advanced integrations.

## Possible extensions

- Connect to meeting transcription services and process recordings automatically  
- Add a Slack or Teams bot that sends tasks directly from chat  
- Use Asana webhooks to send reminders or reports when tasks change  
- Integrate with voice assistants to update tasks by voice  
- Export data for analytics such as completion times or meeting outcome quality

## License

Choose a license for this project, for example MIT, Apache, or another license you prefer.
