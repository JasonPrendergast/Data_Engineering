import sqlite3

# Check if pandas was installed as per instructions
import pip
pkgs  = [package.project_name for package in pip.get_installed_distributions()]

if 'pandas' not in pkgs:
	raise ImportError("Please install pandas in local env")
else:
	print("Existence of pandas checked.")

def get_count(db_file_name, table_name):
	db_conn = sqlite3.connect(db_file_name)
	c = db_conn.cursor()

	c.execute('SELECT count(*) as ct from {tn}'.format(tn=table_name))
	rc = c.fetchone()
	if rc is None:
		raise ValueError('Empty Table' + table_name)
	return rc[0]

def fit(db_file_name, training_table_name):
	count = get_count(db_file_name, training_table_name)
	print('Training with ', count, 'rows complete.')
	return(count)

def test(db_file_name, test_table_name):
	count = get_count(db_file_name, test_table_name)
	print('Testing with ', count, 'rows complete.')
	return(count)