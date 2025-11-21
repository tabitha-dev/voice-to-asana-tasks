from csv_to_asana import load_tasks_with_subtasks, create_tasks_and_subtasks_from_dict

if __name__ == "__main__":
    csv_file_path = "data/samples/tasks_sample.csv"
    csv_out_path = "data/samples/tasks_with_ids_sample.csv"
    tasks = load_tasks_with_subtasks(csv_file_path)
    create_tasks_and_subtasks_from_dict(tasks, csv_out_path)
