import streamlit as st
from config import ICONS

def render_lessons():
    st.markdown(f"<h1 style='display:flex; align-items:center;'>{ICONS.get('book-open', ICONS['book'])}Data Engineering Lessons</h1>", unsafe_allow_html=True)
    st.write("A comprehensive guide to SQL, Data Warehousing, and Modern Table Formats.")
    st.write("---")

    # Chapter 1: SQL Basics
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">1. Database & SQL Basics</h3>
        <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
            A <strong>relational database</strong> organizes data into tables (rows + columns). 
            Tables connect through relationships using <strong>keys</strong>. 
            SQL is the language used to create, query, and manage that data.
        </p>
        <h4 style="color: var(--text-color); margin-top: 20px;">Key Types</h4>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong style="color: #4f8ef7;">Primary Key (PK)</strong><br>
                <span style="font-size: 0.9em; opacity: 0.8;">Unique row identifier. Cannot be NULL. Each row has exactly one. E.g., customer_id.</span>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong style="color: #7c5cbf;">Foreign Key (FK)</strong><br>
                <span style="font-size: 0.9em; opacity: 0.8;">Links two tables. References a PK in another table to create a relationship.</span>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong style="color: #2dbc84;">Composite Key</strong><br>
                <span style="font-size: 0.9em; opacity: 0.8;">Multi-column PK. Two or more columns together uniquely identify a row.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chapter 2: DBMS vs RDBMS
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">2. DBMS vs RDBMS</h3>
        <div style="display: flex; gap: 20px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(79,142,247,0.1); border-radius: 8px;">
                <h4 style="color: #4f8ef7; margin-bottom: 10px;">DBMS</h4>
                <ul style="font-size: 0.9em; opacity: 0.9;">
                    <li>📁 Data stored in files / non-relational format</li>
                    <li>🚫 No relationships between data</li>
                    <li>🔓 Less secure — minimal access control</li>
                    <li>📊 Best for small, simple datasets</li>
                </ul>
            </div>
            <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(45,188,132,0.1); border-radius: 8px;">
                <h4 style="color: #2dbc84; margin-bottom: 10px;">RDBMS</h4>
                <ul style="font-size: 0.9em; opacity: 0.9;">
                    <li>🗂️ Data in tables — rows & columns</li>
                    <li>🔑 Relationships enforced with keys (PK/FK)</li>
                    <li>🔒 Data integrity via ACID properties</li>
                    <li>🏗️ Handles large, complex datasets</li>
                </ul>
            </div>
        </div>
        <p style="font-size: 0.85em; opacity: 0.8; margin-top: 15px; padding-left: 10px; border-left: 2px solid var(--primary-color);">
            <strong>ACID</strong> = Atomicity, Consistency, Isolation, Durability. RDBMS guarantees all four; plain DBMS does not.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Chapter 3: SQL Relationships
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">3. SQL Relationships</h3>
        <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
            Relationships define how tables connect through foreign keys, ensuring <strong>referential integrity</strong>.
        </p>
        <ul style="font-size: 0.95em; opacity: 0.9;">
            <li><strong>One-to-One:</strong> School ↔ Headteacher. FK + UNIQUE.</li>
            <li><strong>One-to-Many:</strong> School ↔ Teacher. FK on the "many" side.</li>
            <li><strong>Many-to-Many:</strong> Pupil ↔ Lesson. Requires a Junction table.</li>
            <li><strong>Self-Ref:</strong> Employee ↔ Manager. FK pointing to its own PK.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Chapter 4: Database Normalization
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">4. Database Normalization</h3>
        <p style="color: var(--text-color); opacity: 0.9; line-height: 1.6;">
            Normalization organizes tables to eliminate redundancy and prevent data anomalies (Insertion, Deletion, Update anomalies).
        </p>
        <table style="width: 100%; border-collapse: collapse; font-size: 0.9em; text-align: left; opacity: 0.9;">
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
                <th style="padding: 8px;">Normal Form</th>
                <th style="padding: 8px;">Rule</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                <td style="padding: 8px;"><strong>1NF</strong></td>
                <td style="padding: 8px;">Atomic values, no repeating column groups, must have a PK.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                <td style="padding: 8px;"><strong>2NF</strong></td>
                <td style="padding: 8px;">No partial dependency on a composite PK.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                <td style="padding: 8px;"><strong>3NF</strong></td>
                <td style="padding: 8px;">No transitive dependency — non-key can't depend on non-key.</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Chapter 5: Data Ecosystem
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">5. The Data Ecosystem</h3>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong>Database</strong><br>
                <span style="font-size: 0.85em; opacity: 0.8;">Operational store. App-specific. Structured. OLTP.</span>
            </div>
            <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong>Data Warehouse</strong><br>
                <span style="font-size: 0.85em; opacity: 0.8;">Analytics hub. Org-wide. Structured. OLAP / BI.</span>
            </div>
            <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong>Data Mart</strong><br>
                <span style="font-size: 0.85em; opacity: 0.8;">Department slice of a warehouse. Inherited schema.</span>
            </div>
            <div style="flex: 1; min-width: 150px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px;">
                <strong>Data Lake</strong><br>
                <span style="font-size: 0.85em; opacity: 0.8;">Raw storage. Any data type. Schema on read.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chapter 6: OLAP vs OLTP
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">6. OLAP vs OLTP</h3>
        <div style="display: flex; gap: 20px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(79,142,247,0.1); border-radius: 8px;">
                <h4 style="color: #4f8ef7; margin-bottom: 10px;">OLTP (Online Transaction Processing)</h4>
                <p style="font-size: 0.9em; opacity: 0.9;">Real-time execution of many short transactions. Apps, banking, shopping carts.</p>
                <p style="font-size: 0.85em; opacity: 0.8;">✓ Fast, ACID, high availability.<br>✗ Limited analytics.</p>
            </div>
            <div style="flex: 1; min-width: 250px; padding: 15px; background: rgba(45,188,132,0.1); border-radius: 8px;">
                <h4 style="color: #2dbc84; margin-bottom: 10px;">OLAP (Online Analytical Processing)</h4>
                <p style="font-size: 0.9em; opacity: 0.9;">Complex read-heavy queries over large historical datasets. BI, recommendations.</p>
                <p style="font-size: 0.85em; opacity: 0.8;">✓ Deep analysis, handles PB data.<br>✗ Complex, batch updates.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chapter 7 & 8: Schemas & SCD
    st.markdown(f"""
    <div class="project-card" style="margin-bottom: 20px; border-left: 5px solid var(--primary-color);">
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">7. Data Warehousing Concepts</h3>
        
        <h4 style="color: var(--text-color); margin-top: 10px;">Star vs Snowflake Schemas</h4>
        <p style="font-size: 0.95em; opacity: 0.9;">
            <strong>Star Schema:</strong> Fact table in the middle, denormalized dimension tables around it. Fast reads, fewer joins.<br>
            <strong>Snowflake Schema:</strong> Dimension tables are normalized (split into sub-tables). Less redundancy, more complex joins.
        </p>

        <h4 style="color: var(--text-color); margin-top: 20px;">Slowly Changing Dimensions (SCD)</h4>
        <ul style="font-size: 0.9em; opacity: 0.9;">
            <li><strong>Type 0:</strong> Fixed. Never changes.</li>
            <li><strong>Type 1:</strong> Overwrite. No history kept.</li>
            <li><strong>Type 2:</strong> New Row. Most common. Full history via surrogate key + valid dates.</li>
            <li><strong>Type 3:</strong> New Column. Adds a "previous_value" column.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
