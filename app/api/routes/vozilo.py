from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.session import get_db
from models import Vozilo  # Import modela vozila
from schemas.vozilo import VoziloCreate, VoziloOut, VoziloUpdate  # Import Pydantic shema

router = APIRouter()

@router.post("/", response_model=VoziloOut)
def create_vozilo_route(vozilo: VoziloCreate, db: Session = Depends(get_db)):
    db_vozilo = Vozilo(**vozilo.dict())
    db.add(db_vozilo)
    db.commit()
    db.refresh(db_vozilo)
    return db_vozilo

@router.get("/{vozilo_id}", response_model=VoziloOut)
def read_vozilo_route(vozilo_id: int, db: Session = Depends(get_db)):
    db_vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if db_vozilo is None:
        raise HTTPException(status_code=404, detail="Vozilo not found")
    return db_vozilo

@router.get("/", response_model=List[VoziloOut])
def read_vozila_route(db: Session = Depends(get_db)):
    vozila = db.query(Vozilo).all()
    return vozila

@router.put("/{vozilo_id}", response_model=VoziloOut)
def update_vozilo_route(vozilo_id: int, vozilo: VoziloUpdate, db: Session = Depends(get_db)):
    db_vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if not db_vozilo:
        raise HTTPException(status_code=404, detail="Vozilo not found")
    update_data = vozilo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_vozilo, key, value)
    db.commit()
    db.refresh(db_vozilo)
    return db_vozilo

@router.delete("/{vozilo_id}")
def delete_vozilo_route(vozilo_id: int, db: Session = Depends(get_db)):
    db_vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if not db_vozilo:
        raise HTTPException(status_code=404, detail="Vozilo not found")
    db.delete(db_vozilo)
    db.commit()
    return {"message": "Vozilo deleted successfully"}
