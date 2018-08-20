# populate the currently configured db with some sample dev data
# does not check if the tables exist
# may create duplicate entries if run multiple times without flushing the db first

db-migrate:
	python manage.py migrate

db-flush:
	python manage.py flush --no-input

db-test-data:
	python manage.py runscript test_data --traceback

db-init: db-migrate db-flush db-test-data
