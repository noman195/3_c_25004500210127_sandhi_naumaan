students=[]
def add():
        sid=input("Student ID: ").strip()
        if any(s["id"]==sid for s in students): print("ID already exists"); return
        students.append({"id":sid,"name":input("Name: ").strip(),"course":input("Course: ").strip(),"marks":float(input("Marks: ") )}); print("Student added")
def display(records=None):
        records=students if records is None else records
        if not records: print("No student records")
        for s in records: print(s["id"],"|",s["name"],"|",s["course"],"|",s["marks"])
def search():
        q=input("Search ID or name: ").lower().strip(); display([s for s in students if s["id"].lower()==q or q in s["name"].lower()])
def update():
        sid=input("ID to update: ").strip()
        for s in students:
            if s["id"]==sid:
                name=input("New name (Enter to keep): ").strip(); course=input("New course (Enter to keep): ").strip(); marks=input("New marks (Enter to keep): ").strip()
                if name: s["name"]=name
                if course: s["course"]=course
                if marks: s["marks"]=float(marks)
                print("Updated"); return
        print("Student not found")
def delete():
        sid=input("ID to delete: ").strip()
        for s in students:
            if s["id"]==sid: students.remove(s); print("Deleted"); return
        print("Student not found")
def sort_records():
        choice=input("1.Sort by name  2.Sort by marks high-to-low: ")
        if choice=="1": display(sorted(students,key=lambda s:s["name"].lower()))
        elif choice=="2": display(sorted(students,key=lambda s:s["marks"],reverse=True))
        else: print("Invalid choice")
while True:
        print("\nCRUD MENU: 1.Add 2.Display 3.Search 4.Update 5.Delete 6.Sort 7.Exit")
        choice=input("Choose: ").strip()
        if choice=="1": add()
        elif choice=="2": display()
        elif choice=="3": search()
        elif choice=="4": update()
        elif choice=="5": delete()
        elif choice=="6": sort_records()
        elif choice=="7": break
        else: print("Invalid choice")