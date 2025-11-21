import csv
import requests
from collections import defaultdict
from config import ASANA_TOKEN, ASANA_PROJECT_ID

HEADERS = {
    "Authorization": f"Bearer {ASANA_TOKEN}",
    "Content-Type": "application/json"
}

def load_tasks_with_subtasks(csv_file_path):
    tasks = defaultdict(list)
    with open(csv_file_path, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (row["task_name"], row["notes"])
            tasks[key].append({
                "subtask_name": row.get("subtask_name", ""),
                "subtask_notes": row.get("subtask_notes", "")
            })
    return tasks

def create_tasks_and_subtasks_from_dict(tasks, csv_out):
    with open(csv_out, "w", newline="", encoding="utf8") as outfile:
        fieldnames = [
            "task_name", "notes", "asana_task_id",
            "subtask_name", "subtask_notes", "asana_subtask_id"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for (task_name, notes), subtasks in tasks.items():
            data = {
                "data": {
                    "name": task_name,
                    "notes": notes,
                    "projects": [ASANA_PROJECT_ID]
                }
            }
            response = requests.post(
                "https://app.asana.com/api/1.0/tasks",
                json=data,
                headers=HEADERS
            )
            result = response.json()
            if response.status_code == 201 and "data" in result:
                task_id = str(result["data"]["gid"])
                print("Created task:", task_name, "Asana ID:", task_id)
            else:
                print("Failed to create task:", task_name, "Response:", result)
                task_id = "ERROR"

            for sub in subtasks:
                if sub["subtask_name"]:
                    subdata = {
                        "data": {
                            "name": sub["subtask_name"],
                            "notes": sub["subtask_notes"]
                        }
                    }
                    subresponse = requests.post(
                        f"https://app.asana.com/api/1.0/tasks/{task_id}/subtasks",
                        json=subdata,
                        headers=HEADERS
                    )
                    subresult = subresponse.json()
                    if subresponse.status_code == 201 and "data" in subresult:
                        sub_id = str(subresult["data"]["gid"])
                        print("   Created subtask:", sub["subtask_name"], "Asana ID:", sub_id)
                    else:
                        print("   Failed subtask:", sub["subtask_name"], "Response:", subresult)
                        sub_id = "ERROR"
                else:
                    sub_id = ""

                writer.writerow({
                    "task_name": task_name,
                    "notes": notes,
                    "asana_task_id": task_id,
                    "subtask_name": sub["subtask_name"],
                    "subtask_notes": sub["subtask_notes"],
                    "asana_subtask_id": sub_id
                })

if __name__ == "__main__":
    csv_file_path = "data/samples/tasks_sample.csv"
    csv_out_path = "data/samples/tasks_with_ids_sample.csv"
    tasks = load_tasks_with_subtasks(csv_file_path)
    create_tasks_and_subtasks_from_dict(tasks, csv_out_path)
