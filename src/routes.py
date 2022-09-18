from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

import models
import service
from database import get_db
from schemas import RequestStatement, Response, StatementSchema

router = APIRouter(prefix="/statements")


@router.get("/")
async def get_statements(db: Session = Depends(get_db)):
    _statements = service.get_statements(db)
    return Response(status="Ok", code="200", message="Success", result=_statements)


@router.get("/{id}/")
async def get_statement_by_id(id: int, db: Session = Depends(get_db)):
    _statement = service.get_statement_by_id(db, id)
    return Response(status="Ok", code="200", message="Success", result=_statement)


@router.get("/game/")
async def get_truths_and_lie(db: Session = Depends(get_db)):
    _statements = service.get_truths_and_lie(db)
    return Response(status="Ok", code="200", message="Success", result=_statements)


@router.patch("/game/{id1}-{id2}-{id3}/")
async def set_statements_used(id1: int, id2: int, id3: int, db: Session = Depends(get_db)):
    service.set_statements_used(id1, id2, id3, db)
    return Response(status="Ok", code="200", message="Success")


@router.patch("/game/reset/")
async def reset_statements(db: Session = Depends(get_db)):
    service.reset_statements(db)
    return Response(status="Ok", code="200", message="Success")


@router.delete("/{id}/")
async def delete_statement_by_id(id: int, db: Session = Depends(get_db)):
    service.delete_statement_by_id(id, db)
    return Response(status="Ok", code="200", message="Success")


@router.delete("/delete/")
async def delete_statement(request: RequestStatement, db: Session = Depends(get_db)):
    service.delete_statement(request.parameter, db)
    return Response(status="Ok", code="200", message="Success")


@router.post("/create/")
async def create_statement(request: RequestStatement, db: Session = Depends(get_db)):
    service.create_statement(request.parameter, db)
    return Response(status="Ok", code="200", message="Success")
