from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

DATABASE_PATH = 'sqlite:///C:\\sqlite\\test.db'

engine = create_engine(DATABASE_PATH, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db(app):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import main.models
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
    Base.metadata.create_all(bind=engine)
    db = SQLAlchemy(app)
    return db
