from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from db.session import get_db  # Pretpostavka o strukturi
from models.vozac import Vozac  # Pretpostavka o strukturi
from schemas.vozac import VozacCreate, VozacOut, VozacUpdate  # Pretpostavka o shemama

router = APIRouter()

@router.post("/", response_model=VozacOut, status_code=201)
def create_vozac(vozac: VozacCreate, db: Session = Depends(get_db)):
    db_vozac = Vozac(**vozac.dict())
    db.add(db_vozac)
    db.commit()
    db.refresh(db_vozac)
    return db_vozac

@router.get("/", response_model=List[VozacOut])
def read_vozaci(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vozaci = db.query(Vozac).offset(skip).limit(limit).all()
    return vozaci

@router.get("/{vozac_id}", response_model=VozacOut)
def read_vozac(vozac_id: int, db: Session = Depends(get_db)):
    vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if vozac is None:
        raise HTTPException(status_code=404, detail="Vozač not found")
    return vozac

@router.put("/{vozac_id}", response_model=VozacOut)
def update_vozac(vozac_id: int, vozac_update: VozacUpdate, db: Session = Depends(get_db)):
    db_vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if not db_vozac:
        raise HTTPException(status_code=404, detail="Vozač not found")
    for key, value in vozac_update.dict(exclude_unset=True).items():
        setattr(db_vozac, key, value)
    db.commit()
    db.refresh(db_vozac)
    return db_vozac

@router.delete("/{vozac_id}", status_code=204)
def delete_vozac(vozac_id: int, db: Session = Depends(get_db)):
    db_vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if not db_vozac:
        raise HTTPException(status_code=404, detail="Vozač not found")
    db.delete(db_vozac)
    db.commit()
    return {"ok": True}
