from database import db_utils

def test_init_db():
    print("✅ Initializing database...")
    db_utils.init_db()

def test_create_entries():
    print("\n✅ Creating sample entries...")
    db_utils.create_entry("First Journal Entry", "Today I learned about SQLite.")
    db_utils.create_entry("Second Entry", "Testing is important.")

def test_get_all_entries():
    print("\n✅ Fetching all entries:")
    entries = db_utils.get_all_entries()
    for entry in entries:
        print(f"[{entry[0]}] {entry[1]} - {entry[2]} (Created at: {entry[3]})")
    return entries

def test_get_entry(entry_id):
    print("\n✅ Testing get_entry():")
    entry = db_utils.get_entry(entry_id)
    print(entry)

def test_update_entry(entry_id):
    print("\n✅ Testing update_entry():")
    db_utils.update_entry(entry_id, "Updated Title", "Updated content for the first entry.")
    test_get_entry(entry_id)

def test_delete_entry(entry_id):
    print("\n✅ Testing delete_entry():")
    db_utils.delete_entry(entry_id)
    print("Remaining entries after deletion:")
    for entry in db_utils.get_all_entries():
        print(entry)

def run_all_tests():
    test_init_db()
    test_create_entries()
    
    entries = test_get_all_entries()

    if entries:
        first_id = entries[0][0]
        test_get_entry(first_id)
        test_update_entry(first_id)
        test_delete_entry(first_id)
    else:
        print("⚠️ No entries to test view/edit/delete on.")

if __name__ == '__main__':
    run_all_tests()
