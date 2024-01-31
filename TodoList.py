import datetime

class TodoList:
    def __init__(self):
        self.tasks_todo = []
        self.tasks_completed = []

    def show_tasks(self):
        print("\nTâches:")
        if not self.tasks_todo and not self.tasks_completed:
            print("Aucune tâche.")
        else:
            print("{:<10s}{:<30s}{:<30s}".format("Index", "Tâches à faire", "Tâches complétées"))
            print("-" * 70)
            for i, (task_todo, task_completed) in enumerate(zip(self.tasks_todo, self.tasks_completed), start=1):
                print("{:<10d}{:<30s}{:<30s}".format(i, task_todo, task_completed))

            if len(self.tasks_todo) > len(self.tasks_completed):
                remaining_tasks = self.tasks_todo[len(self.tasks_completed):]
                for i, task_todo in enumerate(remaining_tasks, start=len(self.tasks_completed)+1):
                    print("{:<10d}{:<30s}".format(i, task_todo))
            elif len(self.tasks_completed) > len(self.tasks_todo):
                remaining_tasks = self.tasks_completed[len(self.tasks_todo):]
                for i, task_completed in enumerate(remaining_tasks, start=len(self.tasks_todo)+1):
                    print("{:<10s}{:<30s}{:<30s}".format("", "", task_completed))

    def add_task(self, task):
        if task.strip():  # Check if task is not empty
            current_date = datetime.datetime.now().date()
            task_with_date = f"{task} (date: {current_date})"
            self.tasks_todo.append(task_with_date)
            print(f"Tâche ajoutée: {task_with_date}")
        else:
            print("La tâche ne peut pas être vide.")

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks_todo.pop(task_index - 1)
            print(f"Tâche supprimée: {deleted_task}")
        except IndexError:
            print("Index de tâche à faire invalide.")

    def complete_task(self, task_index):
        try:
            completed_task = self.tasks_todo.pop(task_index - 1)
            self.tasks_completed.append(completed_task)
            print(f"Tâche complétée: {completed_task}")
        except IndexError:
            print("Index de tâche à faire invalide.")


def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Marquer une tâche comme complète")
        print("5. Quitter")

        choice = input("Choisissez une option (1-5): ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            task = input("Entrez la nouvelle tâche: ")
            todo_list.add_task(task)
        elif choice == "3":
            task_index = int(input("Entrez l'index de la tâche à supprimer: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Entrez l'index de la tâche à marquer comme complète: "))
            todo_list.complete_task(task_index)
        elif choice == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main()
