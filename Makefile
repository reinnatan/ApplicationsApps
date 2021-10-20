#table companies
migration_file:
	python db.py make:migration create_jobs_table --table jobs --create
	python db.py make:migration create_companies_table --table companies --create

	#table applicants
	python db.py make:migration create_applicants_table --table applicants --create
	python db.py make:migration create_applications_table --table applications --create

#make all migrations table
migration_db:
	python db.py migrate