from sqlalchemy import text
from sqlalchemy.orm import Session

from models import Statement
from schemas import StatementSchema


def get_statements(db: Session):
    return db.query(Statement).all()


def get_statement_by_id(id: int, db: Session):
    return db.query(Statement).filter(Statement.id == id).first()


def create_statement(statement: StatementSchema, db: Session):
    _statement = Statement(description=statement.description,
                           truth=statement.truth, backstory=statement.backstory, used=False)
    db.add(_statement)
    db.commit()


def delete_statement_by_id(id: int, db: Session):
    _statement = get_statement_by_id(id, db)
    db.delete(_statement)
    db.commit()


def reset_statement(db: Session):
    _statements = db.query(Statement).filter(Statement.used == True).all()
    for s in _statements:
        s.used = False
    db.commit()


def get_truths_and_lie(db: Session):
    return db.execute(text("SELECT * FROM statements s WHERE s.truth = true AND s.used = false ORDER BY RANDOM () LIMIT 2) UNION (SELECT * FROM statements s WHERE s.truth = false AND s.used = false ORDER BY RANDOM() LIMIT 1"))


def set_statements_used(id1: int, id2: int, id3: int, db: Session):
    _statements = db.query(Statement).filter(
        Statement.id == id1 or Statement.id == id2 or Statement.id == id3).all()
    for s in _statements:
        s.used = True
    db.commit()
