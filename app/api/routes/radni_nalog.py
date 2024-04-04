from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.session import get_db
from models.radni_nalog import RadniNalog
from schemas.radni_nalog import RadniNalogCreate, RadniNalogUpdate, RadniNalogOut

router = APIRouter()

@router.post("/", response_model=RadniNalogOut, status_code=201)
def create_radni_nalog(radni_nalog: RadniNalogCreate, db: Session = Depends(get_db)):
    db_radni_nalog = RadniNalog(**radni_nalog.dict())
    db.add(db_radni_nalog)
    db.commit()
    db.refresh(db_radni_nalog)
    return db_radni_nalog

@router.get("/", response_model=List[RadniNalogOut])
def read_radni_nalozi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    radni_nalozi = db.query(RadniNalog).offset(skip).limit(limit).all()
    return radni_nalozi

@router.get("/{radni_nalog_id}", response_model=RadniNalogOut)
def read_radni_nalog(radni_nalog_id: int, db: Session = Depends(get_db)):
    radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if radni_nalog is None:
        raise HTTPException(status_code=404, detail="Radni nalog not found")
    return radni_nalog

@router.put("/{radni_nalog_id}", response_model=RadniNalogOut)
def update_radni_nalog(radni_nalog_id: int, radni_nalog_update: RadniNalogUpdate, db: Session = Depends(get_db)):
    db_radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if not db_radni_nalog:
        raise HTTPException(status_code=404, detail="Radni nalog not found")
    update_data = radni_nalog_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_radni_nalog, key, value)
    db.commit()
    db.refresh(db_radni_nalog)
    return db_radni_nalog

@router.delete("/{radni_nalog_id}", status_code=204)
def delete_radni_nalog(radni_nalog_id: int, db: Session = Depends(get_db)):
    db_radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if not db_radni_nalog:
        raise HTTPException(status_code=404, detail="Radni nalog not found")
    db.delete(db_radni_nalog)
    db.commit()
    return {"message": "Radni nalog deleted successfully"}
