# seed_all_cs50.py
# Delete and repopulate ALL tables in your DB (CS50-style)
# Requires: pip install cs50

from cs50 import SQL

DB_URL = "sqlite:///clinic.db"  # Change if needed
db = SQL(DB_URL)

db.execute("PRAGMA foreign_keys = ON")

# ===== ORDER MATTERS =====
tables = [
    "appointments",
    "patients",
    "blog_posts",
    "team_members",
    "testimonials",
    "services",
    "clinic_info",
    "users"
]

# --- Wipe all data ---
for table in tables:
    db.execute(f"DELETE FROM {table}")

# Reset AUTOINCREMENT counters
db.execute(f"DELETE FROM sqlite_sequence WHERE name IN ({','.join(['?']*len(tables))})", *tables)

# --- Seed clinic_info ---
db.execute("""
INSERT INTO clinic_info (clinic_name, address, phone_number, email, operating_hours, tagline,
                         facebook_url, instagram_url, twitter_url, maps_embed_url)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
"Zachlice Event Solutions", "123 Event Ave", "555-1010", "info@zachlice.com",
"Mon-Fri 9am-6pm", "Seamless bookings, happy clients.",
"https://facebook.com/zachlice", "https://instagram.com/zachlice", "https://twitter.com/zachlice",
"https://maps.google.com/?q=123+Event+Ave"
)

# --- Seed services ---
services = [
    ("Event Booking", "Plan and reserve event slots effortlessly.", 100, "fas fa-calendar-check"),
    ("Resource Coordination", "Manage venues, equipment and schedules.", 250, "fas fa-tasks"),
    ("On-site Support", "Trained staff for smooth execution.", 500, "fas fa-users"),
]
for name, desc, price, icon in services:
    db.execute(
        "INSERT INTO services (name, description, price, fa_icon_class, is_active) VALUES (?, ?, ?, ?, 1)",
        name, desc, price, icon
    )

# --- Seed testimonials ---
testimonials = [
    ("Perfect event management solution!", "Jamie Cruz", "Corporate Planner", 1),
    ("They made my job so much easier.", "Taylor Brooks", "Wedding Coordinator", 1),
]
for q, a, ad, approved in testimonials:
    db.execute(
        "INSERT INTO testimonials (quote, author_name, author_description, is_approved) VALUES (?, ?, ?, ?)",
        q, a, ad, approved
    )

# --- Seed team_members ---
team = [
    ("Alex Morgan", "CEO", "Event Strategy", "Visionary leader and planner.", "https://picsum.photos/200", 1, 1),
    ("Chris Lee", "Operations Manager", "Logistics", "Ensures smooth operations.", "https://picsum.photos/201", 1, 2),
]
for name, pos, spec, bio, img, active, order in team:
    db.execute(
        "INSERT INTO team_members (name, position, specialization, bio, image_url, is_active, display_order) VALUES (?, ?, ?, ?, ?, ?, ?)",
        name, pos, spec, bio, img, active, order
    )

# --- Seed blog_posts ---
blogs = [
    ("Maximizing Event ROI", "maximizing-event-roi", "Tips for better returns on events.", 1, "https://picsum.photos/800/400", 1),
    ("Why Coordination Matters", "why-coordination-matters", "The backbone of a smooth event.", 1, "https://picsum.photos/801/400", 1),
]
for title, slug, content, author_id, img, published in blogs:
    db.execute(
        "INSERT INTO blog_posts (title, slug, content, author_id, featured_image_url, is_published) VALUES (?, ?, ?, ?, ?, ?)",
        title, slug, content, author_id, img, published
    )

# --- Seed patients ---
patients = [
    ("Jordan White", "jordan@example.com", "555-3333", "male", "1988-05-10", "42 Main St"),
    ("Morgan Black", "morgan@example.com", "555-4444", "female", "1993-09-21", "78 Elm St"),
]
for full_name, email, phone, gender, dob, address in patients:
    db.execute(
        "INSERT INTO patients (full_name, email, phone, gender, date_of_birth, address) VALUES (?, ?, ?, ?, ?, ?)",
        full_name, email, phone, gender, dob, address
    )

# --- Seed appointments ---
appointments = [
    (1, "2025-09-01", "09:00:00", "APPT-001", "Initial consultation", "confirmed"),
    (2, "2025-09-05", "14:30:00", "APPT-002", "Follow-up meeting", "pending"),
]
for pid, date, time, code, msg, status in appointments:
    db.execute(
        "INSERT INTO appointments (patient_id, appointment_date, appointment_time, appointment_code, message, status) VALUES (?, ?, ?, ?, ?, ?)",
        pid, date, time, code, msg, status
    )

# --- Seed users ---
users = [
    ("admin", "admin@example.com", "hashed_password_here", "admin", 1),
    ("staff", "staff@example.com", "hashed_password_here", "staff", 1),
]
for username, email, pwd, role, active in users:
    db.execute(
        "INSERT INTO users (username, email, password_hash, role, is_active) VALUES (?, ?, ?, ?, ?)",
        username, email, pwd, role, active
    )

print("✓ All tables wiped and reseeded successfully.")
