from app import app, db

def verify_database():
    with app.app_context():
        try:
            db.create_all()
            print('Database connection successful')
            print('Tables created successfully')
            
            # List all tables
            print('\nCreated tables:')
            for table in db.metadata.tables.keys():
                print(f'- {table}')
                
        except Exception as e:
            print(f'Error: {str(e)}')

if __name__ == '__main__':
    verify_database()
