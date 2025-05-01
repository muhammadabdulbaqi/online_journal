from database import db_utils

def run_tests():
    print("✅ Initializing database...")
    db_utils.init_db()

    print("\n✅ Creating sample entries...")
    db_utils.create_entry("First Journal Entry", "Today I learned about SQLite.")
    db_utils.create_entry("Second Entry", "Testing is important.")

    print("\n✅ Fetching all entries:")
    entries = db_utils.get_all_entries()
    for entry in entries:
        print(f"[{entry[0]}] {entry[1]} - {entry[2]} (Created at: {entry[3]})")

    if entries:
        print("\n✅ Testing get_entry() for first entry:")
        first_id = entries[0][0]
        entry = db_utils.get_entry(first_id)
        print(entry)

        print("\n✅ Testing update_entry():")
        db_utils.update_entry(first_id, "Updated Title", "Updated content for the first entry.")
        print(db_utils.get_entry(first_id))

        print("\n✅ Testing delete_entry():")
        db_utils.delete_entry(first_id)
        print("Remaining entries after deletion:")
        for entry in db_utils.get_all_entries():
            print(entry)

if __name__ == '__main__':
    run_tests()
