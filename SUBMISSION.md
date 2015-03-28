* A cover page
    - The cover page is found at `project_cover.pdf`
* All the code used in the application
    - Code is in the `src/` folder
* A script that could be used to create all tables and data in the database such as the one here
    - This script is `bootstrapdb.sql`
* A short description of what the project accomplished
    - *An application that allows UBC REC players to sign-up for drop-in sessions in advance to gauge interest!*
* A description of how your final schema differed from the schema you turned in. If the final schema differed, why? Note that turning in a final schema that's different from what you planned is fine, we just want to know what changed and why.
    - There was one schema change made, which was the removal of two fields from the `TeamParticipates_In` table; the `sport_id` field and the `venue_name` fields as they were redundant and already available in the associated Session for that Team.
* A list of the SQL queries used
    - See `src/ubcrec/sqlAPI.py` for queries used.
* List all functional dependencies that are applicable to the table (including the ones involving the primary key). For each functional dependency, briefly describe its meaning in English.
    - The schema is described in `schema_graph.pdf`; we will describe the functional dependencies below.
	- All of our tables are in BCNF, as we have no tables where the key does not determine the other attributes.
    - The 'center' of the schema is the Sessions table. The key, session_id, determines start_time, end_time, sport_id, venue_name, and results.
	- The Sport and Venue tables are 2-column key-value tables, which satisfies 3NF/BCNF. In the Sport table, sport_id determines name, and for the Venue table, venue_name determines address. Because address is stored in a single attribute, there are no explicit additional functional dependencies in this table.
	- In Team_ParticipatesIn, team_id determines the name, number_of_players, and session_id.
	- In PlaysIn, the key, student_num, determines team_id.
	- In Players, the key student_num determines name, password, and salt.
	- In Employees, the key sin determines first_name, last_name, username, password, and salt.
	- In Working, there are no functional dependencies.
