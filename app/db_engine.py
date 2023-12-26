import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create engine singleton
_engine = None
_Session = None
_session = None


def init_engine():
    global _engine
    global _Session
    global _session

    if _engine is None:
        if 'DATABASE_URL' in os.environ:
            _engine = create_engine(os.environ['DATABASE_URL'])
        else:
            _engine = create_engine('sqlite:///app.db')

        _Session = sessionmaker(bind=_engine)
        _session = _Session()


def get_session():
    global _session
    return _session


def close_session():
    global _session
    _session.close()
    _session = None


def get_engine():
    global _engine
    return _engine


def close_engine():
    global _engine
    _engine.dispose()
    _engine = None


init_engine()
