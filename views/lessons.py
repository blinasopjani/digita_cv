import streamlit as st
import textwrap
from config import ICONS

# ─────────────────────────────────────────────────────────────────────────────
# Per-lecture content renderers
# ─────────────────────────────────────────────────────────────────────────────

def _lecture_12():
    """Lecture 12 — Databases, Data Storage & SQL Concepts"""
    # Chapter 1: SQL BASICS
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">1. Database & SQL Basics</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        A <strong>relational database</strong> organizes data into tables (rows + columns). Tables connect through
        relationships using <strong>keys</strong>. SQL is the language used to create, query, and manage that data.
    </p>
</div>
    """), unsafe_allow_html=True)
    st.markdown("#### Essential SQL Commands")
    st.code("""-- Create a table
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    city          VARCHAR(50),
    created_date  DATE
);
-- Insert, Query, Update, Delete
INSERT INTO customers VALUES (1, 'Alice', 'New York', '2024-01-15');
SELECT name, city FROM customers WHERE city = 'New York';
UPDATE customers SET city = 'Boston' WHERE customer_id = 1;
DELETE FROM customers WHERE customer_id = 1;""", language="sql")

    st.markdown(textwrap.dedent("""
<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 24px;">
    <div style="flex:1;min-width:180px;padding:14px;background:rgba(255,255,255,0.05);border-radius:8px;">
        <strong style="color:#4f8ef7;">Primary Key (PK)</strong><br>
        <span style="font-size:0.88em;opacity:0.8;">Unique row identifier. Cannot be NULL.</span>
    </div>
    <div style="flex:1;min-width:180px;padding:14px;background:rgba(255,255,255,0.05);border-radius:8px;">
        <strong style="color:#7c5cbf;">Foreign Key (FK)</strong><br>
        <span style="font-size:0.88em;opacity:0.8;">References a PK in another table to create a relationship.</span>
    </div>
    <div style="flex:1;min-width:180px;padding:14px;background:rgba(255,255,255,0.05);border-radius:8px;">
        <strong style="color:#2dbc84;">Composite Key</strong><br>
        <span style="font-size:0.88em;opacity:0.8;">Two or more columns that together uniquely identify a row.</span>
    </div>
    <div style="flex:1;min-width:180px;padding:14px;background:rgba(255,255,255,0.05);border-radius:8px;">
        <strong style="color:#f0a868;">Super Key</strong><br>
        <span style="font-size:0.88em;opacity:0.8;">Any unique combo of columns that identifies rows.</span>
    </div>
</div>
    """), unsafe_allow_html=True)

    # Chapter 2: DBMS vs RDBMS
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">2. DBMS vs RDBMS</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Before diving into SQL relationships, understand the two types of database management systems.</p>
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 15px;">
        <div style="flex:1;min-width:230px;padding:14px;background:rgba(79,142,247,0.1);border-radius:8px;">
            <h4 style="color:#4f8ef7;margin-bottom:8px;">DBMS</h4>
            <ul style="font-size:0.9em;opacity:0.9;">
                <li>📁 Data stored in files / non-relational format</li>
                <li>🚫 No relationships between data</li>
                <li>🔓 Less secure — minimal access control</li>
                <li>📊 Best for small, simple datasets</li>
                <li>📌 Examples: XML stores, file-based systems</li>
            </ul>
        </div>
        <div style="flex:1;min-width:230px;padding:14px;background:rgba(45,188,132,0.1);border-radius:8px;">
            <h4 style="color:#2dbc84;margin-bottom:8px;">RDBMS</h4>
            <ul style="font-size:0.9em;opacity:0.9;">
                <li>🗂️ Data in tables — rows & columns</li>
                <li>🔑 Relationships enforced with keys (PK/FK)</li>
                <li>🔒 Data integrity via ACID properties</li>
                <li>🏗️ Handles large, complex datasets</li>
                <li>📌 Examples: MySQL, PostgreSQL, Oracle, SQL Server</li>
            </ul>
        </div>
    </div>
    <p style="font-size:0.85em;opacity:0.8;margin-top:14px;padding-left:10px;border-left:3px solid #7c5cbf;">
        <strong>ACID</strong> = Atomicity · Consistency · Isolation · Durability. RDBMS guarantees all four.
    </p>
</div>
    """), unsafe_allow_html=True)

    # Chapter 3: RELATIONSHIPS
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">3. SQL Relationships</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        Relationships define how tables connect through foreign keys, ensuring <strong>referential integrity</strong>.
    </p>
    <ul style="font-size:0.95em;opacity:0.9;margin-bottom:14px;">
        <li><strong>One-to-One:</strong> School ↔ Headteacher. (FK + UNIQUE)</li>
        <li><strong>One-to-Many:</strong> School ↔ Teacher. (FK on "many" side)</li>
        <li><strong>Many-to-Many:</strong> Pupil ↔ Lesson. (Requires a Junction table)</li>
        <li><strong>Self-Ref:</strong> Employee ↔ Manager. (FK points to own PK)</li>
    </ul>
</div>
    """), unsafe_allow_html=True)
    st.markdown("#### Many-to-Many — Junction Table Example")
    st.code("""CREATE TABLE students (student_id INT PRIMARY KEY, name VARCHAR(50));
CREATE TABLE courses  (course_id  INT PRIMARY KEY, name VARCHAR(50));

CREATE TABLE student_courses (
    student_id INT REFERENCES students(student_id),
    course_id  INT REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
);""", language="sql")

    # Chapter 4: NORMALIZATION
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">4. Database Normalization</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        Normalization eliminates redundancy and prevents data anomalies through progressive <strong>Normal Forms</strong>.
    </p>
    <table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:left;opacity:0.9;margin-top:14px;">
        <tr style="border-bottom:1px solid rgba(255,255,255,0.2);">
            <th style="padding:8px;">Normal Form</th><th style="padding:8px;">Rule</th><th style="padding:8px;">What it Fixes</th>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>1NF</strong></td><td style="padding:8px;">Atomic values, PK required</td><td style="padding:8px;">Arrays in cells</td>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>2NF</strong></td><td style="padding:8px;">No partial dependency on composite PK</td><td style="padding:8px;">Partial key dependencies</td>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>3NF</strong></td><td style="padding:8px;">No transitive dependency</td><td style="padding:8px;">Non-key depends on non-key</td>
        </tr>
        <tr><td style="padding:8px;"><strong>BCNF</strong></td><td style="padding:8px;">Every determinant = candidate key</td><td style="padding:8px;">Edge cases 3NF misses</td></tr>
    </table>
</div>
    """), unsafe_allow_html=True)
    st.markdown("#### 3NF Example — Before & After")
    st.code("""-- PROBLEM: dept_name depends on dept_num, not on emp_num (PK)
CREATE TABLE employee   (emp_num INT PRIMARY KEY, fname VARCHAR, lname VARCHAR);
CREATE TABLE department (dept_num VARCHAR PRIMARY KEY, dept_name VARCHAR);
CREATE TABLE emp_dept   (emp_num INT REFERENCES employee, dept_num VARCHAR REFERENCES department);""", language="sql")

    # Chapter 5: DATA ECOSYSTEM
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">5. The Data Ecosystem</h3>
    <p style="color: var(--text-color); opacity: 0.9;">DB vs Warehouse vs Mart vs Lake — each serves a different purpose in the data lifecycle.</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:14px;">
        <div style="flex:1;min-width:140px;padding:14px;background:rgba(79,142,247,0.1);border-radius:8px;">
            <strong style="color:#4f8ef7;">Database</strong><br>
            <span style="font-size:0.85em;opacity:0.8;">Operational. App-specific. OLTP.</span>
        </div>
        <div style="flex:1;min-width:140px;padding:14px;background:rgba(45,188,132,0.1);border-radius:8px;">
            <strong style="color:#2dbc84;">Data Warehouse</strong><br>
            <span style="font-size:0.85em;opacity:0.8;">Analytics Hub. Org-wide. OLAP.</span>
        </div>
        <div style="flex:1;min-width:140px;padding:14px;background:rgba(124,92,191,0.1);border-radius:8px;">
            <strong style="color:#7c5cbf;">Data Mart</strong><br>
            <span style="font-size:0.85em;opacity:0.8;">Department Slice of a Warehouse.</span>
        </div>
        <div style="flex:1;min-width:140px;padding:14px;background:rgba(240,168,104,0.1);border-radius:8px;">
            <strong style="color:#f0a868;">Data Lake</strong><br>
            <span style="font-size:0.85em;opacity:0.8;">Raw Storage. Any format. Schema on read.</span>
        </div>
    </div>
</div>
    """), unsafe_allow_html=True)

    # Chapter 6: OLAP vs OLTP
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">6. OLAP vs OLTP</h3>
    <p style="color: var(--text-color); opacity: 0.9;">The two dominant processing paradigms — most organizations run both in parallel.</p>
    <table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:left;opacity:0.9;margin-top:14px;">
        <tr style="border-bottom:1px solid rgba(255,255,255,0.2);">
            <th style="padding:8px;">Category</th>
            <th style="padding:8px;color:#2dbc84;">OLAP (Analytical)</th>
            <th style="padding:8px;color:#4f8ef7;">OLTP (Transactional)</th>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>Data source</strong></td>
            <td style="padding:8px;">Historical, multiple databases</td>
            <td style="padding:8px;">Current operational data</td>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>Purpose</strong></td>
            <td style="padding:8px;">Analysis & BI</td>
            <td style="padding:8px;">Day-to-day transactions</td>
        </tr>
        <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <td style="padding:8px;"><strong>Normalization</strong></td>
            <td style="padding:8px;">Denormalized (Star/Snowflake)</td>
            <td style="padding:8px;">Normalized (3NF)</td>
        </tr>
        <tr>
            <td style="padding:8px;"><strong>Query type</strong></td>
            <td style="padding:8px;">Complex, read-heavy</td>
            <td style="padding:8px;">Simple, read/write (fast)</td>
        </tr>
    </table>
</div>
    """), unsafe_allow_html=True)

    # Chapter 7: SCHEMAS
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">7. Star Schema vs Snowflake Schema</h3>
    <p style="color: var(--text-color); opacity: 0.9;">A central <strong>Fact Table</strong> (events) surrounded by <strong>Dimension Tables</strong> (context).</p>
    <h4 style="color:#f0a868;margin-top:18px;">Star Schema</h4>
    <p style="font-size:0.9em;opacity:0.9;">Flat, denormalized dimensions. Fewer JOINs → faster reads.</p>
    <h4 style="color:#f0a868;margin-top:12px;">Snowflake Schema</h4>
    <p style="font-size:0.9em;opacity:0.9;">Normalized dimensions split into sub-tables. Less redundancy, more JOINs.</p>
</div>
    """), unsafe_allow_html=True)

    # Chapter 8: SCD
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">8. Slowly Changing Dimensions (SCD)</h3>
    <p style="color: var(--text-color); opacity: 0.9;">How to handle dimension data that changes over time while preserving historical accuracy.</p>
    <ul style="font-size:0.95em;opacity:0.9;">
        <li><strong>Type 0 (Fixed):</strong> Immutable. Never changes (e.g. DOB).</li>
        <li><strong>Type 1 (Overwrite):</strong> Old value replaced. No history kept.</li>
        <li><strong>Type 2 (New Row):</strong> Most common. New record per change. Full history.</li>
        <li><strong>Type 3 (New Column):</strong> Adds a previous_value column. One prior value only.</li>
        <li><strong>Type 4 (History Table):</strong> Current in main table; history in separate table.</li>
        <li><strong>Type 6 (Hybrid):</strong> Combines Types 1 + 2 + 3.</li>
    </ul>
</div>
    """), unsafe_allow_html=True)
    st.markdown("#### Type 2 — Example")
    st.code("""UPDATE dim_customer SET end_date='2024-06-01', is_current=FALSE WHERE customer_id=101 AND is_current=TRUE;
INSERT INTO dim_customer VALUES (2, 101, 'Amir', 'Mumbai', '2024-06-01', NULL, TRUE);
-- surr | cust | city   | start      | end        | current
-- 1    | 101  | Delhi  | 2020-01-01 | 2024-06-01 | FALSE  ← history
-- 2    | 101  | Mumbai | 2024-06-01 | NULL       | TRUE   ← current""", language="sql")

    # Chapter 9: APACHE ICEBERG
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">9. Apache Iceberg: Spark SQL vs DataFrames</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Iceberg is a modern open table format for huge datasets. Use <strong>Spark SQL</strong> or the <strong>DataFrame API</strong>.</p>
</div>
    """), unsafe_allow_html=True)
    st.markdown("#### Session Setup")
    st.code("""from pyspark.sql import SparkSession
spark = SparkSession.builder \\
  .appName("IcebergDemo") \\
  .config('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2') \\
  .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \\
  .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \\
  .config("spark.sql.catalog.local.type", "hadoop") \\
  .getOrCreate()""", language="python")
    tab1, tab2, tab3 = st.tabs(["Create & Append", "Query & Schema", "Delete"])
    with tab1:
        st.code("""spark.sql("CREATE TABLE local.sql.data_points (id INT, name STRING, value INT) USING iceberg")
spark.sql("INSERT INTO local.sql.data_points VALUES (1,'metric_1',5),(2,'metric_2',10)")""", language="python")
    with tab2:
        st.code("""spark.sql("SELECT * FROM local.sql.data_points WHERE name='metric_1' ORDER BY id").show()
spark.sql("ALTER TABLE local.sql.data_points ADD COLUMNS (source STRING)")""", language="python")
    with tab3:
        st.code("""spark.sql("DELETE FROM local.sql.data_points WHERE source = 'source_1'")""", language="python")

    # Conclusion
    st.markdown(textwrap.dedent("""
<div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">10. How It All Connects</h3>
    <p style="color: var(--text-color); opacity: 0.9; margin-bottom: 14px;">
        <strong>RDBMS / OLTP</strong> (3NF, ACID)
        <span style="color:#ff4d8d;">→</span> <strong>ETL / Spark</strong> (SCD, Iceberg)
        <span style="color:#ff4d8d;">→</span> <strong>Data Warehouse</strong> (Star/Snowflake, OLAP)
        <span style="color:#ff4d8d;">→</span> <strong>Data Lake</strong> (Iceberg)
        <span style="color:#ff4d8d;">→</span> <strong>BI Tools</strong> (Power BI, Tableau)
    </p>
</div>
    """), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Lecture registry  — add new lectures here
# ─────────────────────────────────────────────────────────────────────────────
LECTURES = [
    {
        "label": "Lecture 12 — Databases, Data Storage & SQL Concepts",
        "icon": "📋",
        "render": _lecture_12,
    },
    # Add more lectures here as needed:
    # {
    #     "label": "Lecture 13 — ...",
    #     "icon": "📋",
    #     "render": _lecture_13,
    # },
]


# ─────────────────────────────────────────────────────────────────────────────
# Main render function
# ─────────────────────────────────────────────────────────────────────────────
def render_lessons():
    # Header
    st.markdown(
        f"<h1 style='display:flex;align-items:center;gap:10px;'>"
        f"{ICONS.get('book', '📚')} Lessons</h1>",
        unsafe_allow_html=True,
    )
    st.write("Summaries of lecture content, organized by lecture number.")
    st.write("---")

    # Jump-to dropdown
    lecture_labels = ["All"] + [lec["label"] for lec in LECTURES]
    st.markdown("**Jump to a lecture**")
    selected = st.selectbox("Select a lecture:", lecture_labels)

    st.write("")  # spacer

    # Render lectures as expanders
    for lec in LECTURES:
        if selected == "All" or selected == lec["label"]:
            with st.expander(f"{lec['icon']} {lec['label']}"):
                lec["render"]()
