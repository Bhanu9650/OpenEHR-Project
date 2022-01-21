app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:abc123@localhost:5432/eapr"
db = SQLAlchemy(app)