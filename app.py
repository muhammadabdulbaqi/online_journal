import streamlit as st
import requests

API_URL = "http://localhost:5000/api/entries"

st.set_page_config(page_title="📓 Online Journal", layout="centered")
st.title("📓 My Online Journal")

# --- Helper: Update Entry ---
def update_entry(entry_id, title, content):
    payload = {"title": title, "content": content}
    return requests.put(f"{API_URL}/{entry_id}", json=payload)

# --- Helper: Delete Entry ---
def delete_entry(entry_id):
    return requests.delete(f"{API_URL}/{entry_id}")

# --- Display All Entries ---
def display_entries():
    st.header("📄 All Journal Entries")

    try:
        response = requests.get(API_URL)
        entries = response.json()

        if not entries:
            st.info("No journal entries found.")
        else:
            for entry in entries:  # Preserve DB order
                with st.expander(f"{entry['title']}  —  🕒 {entry['created_at']}"):
                    st.markdown(entry["content"])

                    # --- Edit ---
                    edit_key = f"edit_{entry['id']}"
                    if st.button("✏️ Edit Entry", key=edit_key):
                        st.session_state[f"edit_mode_{entry['id']}"] = True

                    if st.session_state.get(f"edit_mode_{entry['id']}", False):
                        new_title = st.text_input("Title", value=entry["title"], key=f"title_{entry['id']}")
                        new_content = st.text_area("Content", value=entry["content"], key=f"content_{entry['id']}")
                        if st.button("Update Entry", key=f"update_{entry['id']}"):
                            res = update_entry(entry["id"], new_title, new_content)
                            if res.status_code == 200:
                                st.success("Entry updated!")
                                st.rerun()
                            else:
                                st.error("Update failed.")

                    # --- Delete ---
                    if st.button("🗑 Delete Entry", key=f"delete_{entry['id']}"):
                        res = delete_entry(entry["id"])
                        if res.status_code == 204:
                            st.success("Entry deleted.")
                            st.rerun()
                        else:
                            st.error("Deletion failed.")

    except Exception as e:
        st.error(f"Failed to fetch entries: {e}")

# --- Add Entry Form ---
def add_entry_form():
    st.header("➕ Add a New Entry")

    # Show success message after rerun
    if st.session_state.get("entry_created", False):
        st.success("✅ Entry created successfully!")
        st.session_state.entry_created = False  # reset flag

    with st.form("entry_form"):
        title = st.text_input("Title", key="form_title")
        content = st.text_area("Content", key="form_content")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not title or not content:
                st.warning("Title and content are required.")
            else:
                try:
                    payload = {"title": title, "content": content}
                    res = requests.post(API_URL, json=payload)

                    if res.status_code == 201:
                        # Set success flag, rerun app
                        st.session_state.entry_created = True
                        st.rerun()  # Rerun clears old form values naturally
                    else:
                        st.error(f"Failed to create entry: {res.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")


# --- Page Navigation ---
page = st.sidebar.radio("Navigate", ["📄 View Entries", "➕ Add Entry"])
if page == "📄 View Entries":
    display_entries()
elif page == "➕ Add Entry":
    add_entry_form()
