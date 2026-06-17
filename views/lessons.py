import streamlit as st
import textwrap
from config import ICONS

def render_lessons():
    st.markdown(f"<h1 style='display:flex; align-items:center;'>{ICONS.get('book-open', ICONS['book'])}Data Engineering Guide</h1>", unsafe_allow_html=True)
    st.write("Complete Reference: From relational databases to data lakes, warehouses, and modern table formats.")
    st.write("---")

    # Chapter 1: SQL BASICS
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">1. Database & SQL Basics</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        A <strong>relational database</strong> organizes data into tables (rows + columns). Tables connect through relationships using <strong>keys</strong>. SQL is the language used to create, query, and manage that data.
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

    st.markdown(textwrap.dedent(f"""
<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 30px;">
    <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
        <strong style="color: #4f8ef7;">Primary Key (PK)</strong><br>
        <span style="font-size: 0.9em; opacity: 0.8;">Unique row identifier. Cannot be NULL. Each row has exactly one.</span>
    </div>
    <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
        <strong style="color: #7c5cbf;">Foreign Key (FK)</strong><br>
        <span style="font-size: 0.9em; opacity: 0.8;">Links two tables. References a PK in another table to create a relationship.</span>
    </div>
    <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
        <strong style="color: #2dbc84;">Composite Key</strong><br>
        <span style="font-size: 0.9em; opacity: 0.8;">Multi-column PK. Two or more columns together uniquely identify a row.</span>
    </div>
    <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
        <strong style="color: #f0a868;">Super Key</strong><br>
        <span style="font-size: 0.9em; opacity: 0.8;">Any unique combo of columns that uniquely identifies rows.</span>
    </div>
</div>
    """), unsafe_allow_html=True)

    # Chapter 2: DBMS vs RDBMS
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">2. DBMS vs RDBMS</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Before diving into SQL relationships, it helps to understand the two types of database management systems and how they differ.</p>
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 15px;">
        <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(79,142,247,0.1); border-radius: 8px;">
            <h4 style="color: #4f8ef7; margin-bottom: 10px;">DBMS</h4>
            <ul style="font-size: 0.9em; opacity: 0.9;">
                <li>📁 Data stored in files / non-relational format</li>
                <li>🚫 No relationships between data</li>
                <li>🔓 Less secure — minimal access control</li>
                <li>📊 Best for small, simple datasets</li>
                <li>📌 Examples: XML stores, file-based systems</li>
            </ul>
        </div>
        <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(45,188,132,0.1); border-radius: 8px;">
            <h4 style="color: #2dbc84; margin-bottom: 10px;">RDBMS</h4>
            <ul style="font-size: 0.9em; opacity: 0.9;">
                <li>🗂️ Data in tables — rows & columns</li>
                <li>🔑 Relationships enforced with keys (PK/FK)</li>
                <li>🔒 Data integrity via ACID properties</li>
                <li>🏗️ Handles large, complex datasets</li>
                <li>📌 Examples: MySQL, PostgreSQL, Oracle, SQL Server</li>
            </ul>
        </div>
    </div>
    <p style="font-size: 0.85em; opacity: 0.8; margin-top: 15px; padding-left: 10px; border-left: 3px solid #7c5cbf;">
        <strong>ACID</strong> = Atomicity (all or nothing), Consistency (rules always apply), Isolation (transactions don't interfere), Durability (committed data survives crashes). RDBMS guarantees all four; plain DBMS does not.
    </p>
</div>
    """), unsafe_allow_html=True)

    # Chapter 3: RELATIONSHIPS
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">3. SQL Relationships</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        Relationships define how tables connect through foreign keys, ensuring <strong>referential integrity</strong> — you can't have an order for a customer that doesn't exist.
    </p>
    <ul style="font-size: 0.95em; opacity: 0.9; margin-bottom: 15px;">
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

-- Junction table bridges the many-to-many
CREATE TABLE student_courses (
    student_id INT REFERENCES students(student_id),
    course_id  INT REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)  -- composite PK
);""", language="sql")

    # Chapter 4: NORMALIZATION
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">4. Database Normalization</h3>
    <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
        Normalization organizes tables to eliminate redundancy and prevent data anomalies. Applied progressively through <strong>Normal Forms</strong>.
    </p>
    <p style="font-size: 0.85em; opacity: 0.8; margin-top: 15px; padding-left: 10px; border-left: 3px solid var(--primary-color);">
        <strong>3 Anomalies Prevented:</strong> Insertion (can't add data without unrelated data) · Deletion (removing a row loses other important data) · Update (changing one copy doesn't update duplicates).
    </p>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.9em; text-align: left; opacity: 0.9; margin-top: 15px;">
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
            <th style="padding: 8px;">Normal Form</th>
            <th style="padding: 8px;">Rule</th>
            <th style="padding: 8px;">What it Fixes</th>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>1NF</strong></td>
            <td style="padding: 8px;">Atomic values, no repeating column groups, must have a PK</td>
            <td style="padding: 8px;">Arrays in cells, duplicate column sets</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>2NF</strong></td>
            <td style="padding: 8px;">No partial dependency on a composite PK</td>
            <td style="padding: 8px;">Non-key column depends on only part of the composite PK</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>3NF</strong></td>
            <td style="padding: 8px;">No transitive dependency</td>
            <td style="padding: 8px;">Non-key depends on non-key</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>BCNF</strong></td>
            <td style="padding: 8px;">Every determinant must be a candidate key</td>
            <td style="padding: 8px;">Edge cases 3NF misses</td>
        </tr>
    </table>
</div>
    """), unsafe_allow_html=True)

    st.markdown("#### 3NF Example — Before & After")
    st.code("""-- PROBLEM: dept_name depends on dept_num, not on emp_num (the PK)
-- emp_num | name  | dept_num | dept_name  ← redundant, causes update anomaly

-- SOLUTION: Split into 3 tables
CREATE TABLE employee   (emp_num INT PRIMARY KEY, fname VARCHAR, lname VARCHAR);
CREATE TABLE department (dept_num VARCHAR PRIMARY KEY, dept_name VARCHAR);
CREATE TABLE emp_dept   (emp_num INT REFERENCES employee, dept_num VARCHAR REFERENCES department);""", language="sql")

    # Chapter 5: DATA ECOSYSTEM
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">5. The Data Ecosystem</h3>
    <p style="color: var(--text-color); opacity: 0.9;">DB vs Warehouse vs Mart vs Lake: Not all data storage is the same. Each system serves a different purpose in the data lifecycle.</p>
    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 15px;">
        <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(79,142,247,0.1); border-radius: 8px;">
            <strong style="color: #4f8ef7;">Database</strong><br>
            <span style="font-size: 0.85em; opacity: 0.8;">Operational Store. App-specific. Structured. Schema on write. For OLTP.</span>
        </div>
        <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(45,188,132,0.1); border-radius: 8px;">
            <strong style="color: #2dbc84;">Data Warehouse</strong><br>
            <span style="font-size: 0.85em; opacity: 0.8;">Analytics Hub. Org-wide. Structured. Schema on write. For BI / OLAP.</span>
        </div>
        <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(124,92,191,0.1); border-radius: 8px;">
            <strong style="color: #7c5cbf;">Data Mart</strong><br>
            <span style="font-size: 0.85em; opacity: 0.8;">Department Slice. Subset of a warehouse. Specific business function analysis.</span>
        </div>
        <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(240,168,104,0.1); border-radius: 8px;">
            <strong style="color: #f0a868;">Data Lake</strong><br>
            <span style="font-size: 0.85em; opacity: 0.8;">Raw Storage. Any data type (structured, semi, un). Schema on read. Big data.</span>
        </div>
    </div>
</div>
    """), unsafe_allow_html=True)

    # Chapter 6: OLAP vs OLTP
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">6. OLAP vs OLTP</h3>
    <p style="color: var(--text-color); opacity: 0.9;">The two dominant processing paradigms — most organizations run both in parallel.</p>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.9em; text-align: left; opacity: 0.9; margin-top: 15px;">
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
            <th style="padding: 8px;">Category</th>
            <th style="padding: 8px; color: #2dbc84;">OLAP (Analytical)</th>
            <th style="padding: 8px; color: #4f8ef7;">OLTP (Transactional)</th>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>Data source</strong></td>
            <td style="padding: 8px;">Historical, multiple databases</td>
            <td style="padding: 8px;">Current operational data</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>Purpose</strong></td>
            <td style="padding: 8px;">Analysis & decision-making (BI)</td>
            <td style="padding: 8px;">Day-to-day transactions</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>Normalization</strong></td>
            <td style="padding: 8px;">Not normalized (Star/Snowflake)</td>
            <td style="padding: 8px;">Normalized (3NF)</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <td style="padding: 8px;"><strong>Query type</strong></td>
            <td style="padding: 8px;">Complex, read-heavy (slow)</td>
            <td style="padding: 8px;">Simple, read/write (fast)</td>
        </tr>
    </table>
</div>
    """), unsafe_allow_html=True)

    # Chapter 7: SCHEMAS
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">7. Star Schema vs Snowflake Schema</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Data warehouse schemas use a central <strong>Fact Table</strong> (measurable events) surrounded by <strong>Dimension Tables</strong> (context: who, what, when, where).</p>
    <h4 style="color: #f0a868; margin-top: 20px;">Star Schema</h4>
    <p style="font-size: 0.9em; opacity: 0.9;">Dimensions are flat and denormalized. Directly linked to the Fact table. Less joins, faster reads.</p>
    <h4 style="color: #f0a868; margin-top: 15px;">Snowflake Schema</h4>
    <p style="font-size: 0.9em; opacity: 0.9;">Dimensions split into sub-tables (Normalized). E.g., Customer → City → Region. Less redundancy, more JOINs.</p>
</div>
    """), unsafe_allow_html=True)

    st.markdown("#### Star Schema Example")
    st.code("""-- Star Schema Example: Denormalized dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR,
    city_name VARCHAR,
    region_name VARCHAR,
    country VARCHAR
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT REFERENCES dim_customer,
    amount DECIMAL
);""", language="sql")

    st.markdown("#### Snowflake Schema Example")
    st.code("""-- Snowflake Schema Example: Normalized dimensions
CREATE TABLE dim_region   (region_id INT PRIMARY KEY, region_name VARCHAR, country VARCHAR);
CREATE TABLE dim_city     (city_id INT PRIMARY KEY, city_name VARCHAR, region_id INT REFERENCES dim_region);
CREATE TABLE dim_customer (customer_id INT PRIMARY KEY, name VARCHAR, city_id INT REFERENCES dim_city);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT REFERENCES dim_customer,
    amount DECIMAL
);""", language="sql")

    # Chapter 8: SCD
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">8. Slowly Changing Dimensions (SCD)</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Dimension data changes over time. SCDs define how to handle those changes while preserving historical accuracy.</p>
</div>
    """), unsafe_allow_html=True)
    
    with st.expander("Type 0 (Fixed)"):
        st.write("Immutable. The value never changes (e.g. Date of Birth). If a source system sends an update, it is ignored or raises an error.")
        st.code("""-- Ignore incoming changes
-- No SQL operation is performed when data changes in the source.""", language="sql")

    with st.expander("Type 1 (Overwrite)"):
        st.write("Old value is replaced. No history is kept. Used for fixing typos or when history doesn't matter.")
        st.code("""-- When customer Amir moves from Delhi to Mumbai
UPDATE dim_customer 
SET city = 'Mumbai' 
WHERE customer_id = 101;

-- Result: Only 'Mumbai' exists. 'Delhi' is lost forever.""", language="sql")

    with st.expander("Type 2 (New Row)"):
        st.write("Most common method. A new record is inserted per change. Full history is preserved using a surrogate key, start/end dates, and a current flag.")
        st.code("""-- 1. Expire the old row
UPDATE dim_customer
SET end_date = '2024-06-01', is_current = FALSE
WHERE customer_id = 101 AND is_current = TRUE;

-- 2. Insert the new row
INSERT INTO dim_customer (surr_key, customer_id, name, city, start_date, end_date, is_current)
VALUES (2, 101, 'Amir', 'Mumbai', '2024-06-01', NULL, TRUE);

-- surr | cust | city   | start      | end        | current
-- 1    | 101  | Delhi  | 2020-01-01 | 2024-06-01 | FALSE  ← history
-- 2    | 101  | Mumbai | 2024-06-01 | NULL       | TRUE   ← current""", language="sql")

    with st.expander("Type 3 (New Column)"):
        st.write("Adds a specific column to keep the immediate previous value. Limited history (only keeps the last change).")
        st.code("""-- Move current city to previous_city, then update current city
UPDATE dim_customer 
SET previous_city = current_city, 
    current_city = 'Mumbai' 
WHERE customer_id = 101;

-- cust | previous_city | current_city
-- 101  | Delhi         | Mumbai""", language="sql")

    with st.expander("Type 4 (History Table)"):
        st.write("Keeps the main dimension table small by only storing the current state, while moving all historical states to a separate history table.")
        st.code("""-- 1. Archive the current state into the history table
INSERT INTO dim_customer_history 
SELECT * FROM dim_customer WHERE customer_id = 101;

-- 2. Overwrite the state in the main table
UPDATE dim_customer 
SET city = 'Mumbai' 
WHERE customer_id = 101;""", language="sql")

    with st.expander("Type 6 (Hybrid)"):
        st.write("Combines Type 1, 2, and 3. Adds a new row for history (Type 2), stores the previous value in a column (Type 3), and overwrites the 'current value' across all historical rows (Type 1) for easy querying.")
        st.code("""-- Very complex to implement.
-- Notice how 'current_city' is Mumbai for both rows, allowing us to group by the current state even on historical rows.

-- surr | cust | hist_city | current_city | start      | end        | current
-- 1    | 101  | Delhi     | Mumbai       | 2020-01-01 | 2024-06-01 | FALSE
-- 2    | 101  | Mumbai    | Mumbai       | 2024-06-01 | NULL       | TRUE""", language="sql")

    # Chapter 9: APACHE ICEBERG
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">9. Apache Iceberg: Spark SQL vs DataFrames</h3>
    <p style="color: var(--text-color); opacity: 0.9;">Iceberg is a modern open table format for huge datasets. You can use <strong>Spark SQL</strong> (familiar) or <strong>DataFrame API</strong> (programmatic).</p>
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
        st.code("""### Spark SQL ###
spark.sql("CREATE TABLE local.sql.data_points (id INT, name STRING, value INT) USING iceberg")
spark.sql("INSERT INTO local.sql.data_points VALUES (1,'metric_1',5),(2,'metric_2',10)")

### DataFrame API ###
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
schema = StructType([StructField("id", IntegerType()), StructField("name", StringType()), StructField("value", IntegerType())])
data = [(1,'metric_1',5), (2,'metric_2',10)]
df = spark.createDataFrame(data, schema)
df.writeTo("local.df.data_points").using("iceberg").create()""", language="python")
    with tab2:
        st.code("""### Query - Spark SQL ###
spark.sql("SELECT * FROM local.sql.data_points WHERE name='metric_1' ORDER BY id").show()

### Query - DataFrame API ###
import pyspark.sql.functions as F
spark.read.format("iceberg").table("local.df.data_points") \\
  .where(F.col("name").eqNullSafe("metric_1")).orderBy('id').show()

### Schema Evolution ###
# SQL
spark.sql("ALTER TABLE local.sql.data_points ADD COLUMNS (source STRING)")
# DF
evolved_df = append_df.withColumn("source", F.lit(None).cast(StringType()))
evolved_df.writeTo("local.df.data_points").option("mergeSchema", "true").using("iceberg").append()""", language="python")
    with tab3:
        st.code("""### Delete - Spark SQL ###
spark.sql("DELETE FROM local.sql.data_points WHERE source = 'source_1'")

### Delete - DataFrame API ###
# No direct delete primitive — filter to keep, then replace
keep_df = transformed_df.where(F.col("source") != "source_1")
keep_df.writeTo("local.df.data_points").option("mergeSchema","true").using("iceberg").replace()""", language="python")

    # Conclusion: How It All Connects
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; justify-content: flex-start; margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
    <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">How It All Connects</h3>
    <p style="color: var(--text-color); opacity: 0.9; margin-bottom: 15px;">
        <strong>RDBMS / OLTP</strong> (Normalized 3NF, ACID) 
        <span style="color: #ff4d8d;">→</span> <strong>ETL / Spark</strong> (SCD logic, Iceberg format) 
        <span style="color: #ff4d8d;">→</span> <strong>Data Warehouse</strong> (Star/Snowflake, OLAP queries) 
        <span style="color: #ff4d8d;">→</span> <strong>Data Lake</strong> (Raw + structured via Iceberg) 
        <span style="color: #ff4d8d;">→</span> <strong>BI Tools</strong> (Power BI, Tableau)
    </p>
</div>
    """), unsafe_allow_html=True)
