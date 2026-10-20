resources = []


def add_resource():
    title = input("Resource title: ").strip()
    category = input("Category (Notes/Books/Links/Other): ").strip()
    link = input("URL or resource location: ").strip()

    if not title or not category or not link:
        print("All fields are required.")
        return

    resources.append({
        "title": title,
        "category": category,
        "link": link
    })
    print("Resource added successfully!")


def view_resources(items=None):
    items = resources if items is None else items

    if not items:
        print("No resources found.")
        return

    for index, item in enumerate(items, start=1):
        print(f"\n{index}. {item['title']}")
        print(f"   Category: {item['category']}")
        print(f"   Location: {item['link']}")


def search_resources():
    keyword = input("Search title or category: ").strip().lower()
    results = [
        item for item in resources
        if keyword in item["title"].lower()
        or keyword in item["category"].lower()
    ]
    view_resources(results)


def main():
    while True:
        print("\nCAMPUS RESOURCE ORGANIZER")
        print("1. Add resource")
        print("2. View resources")
        print("3. Search resources")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resource()
        elif choice == "2":
            view_resources()
        elif choice == "3":
            search_resources()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
