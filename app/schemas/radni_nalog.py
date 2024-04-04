from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .vozac import VozacOut  # Pretpostavka da imate ovu shemu
from .vozilo import VoziloOut  # Pretpostavka da imate ovu shemu

class RadniNalogBase(BaseModel):
    opis_zadatka: str
    datum_i_vrijeme_izdavanja: Optional[datetime] = None
    rok_zavrsavanja: Optional[datetime] = None
    status: str

class RadniNalogCreate(RadniNalogBase):
    vozilo_id: int
    vozac_id: int

class RadniNalogUpdate(BaseModel):
    opis_zadatka: Optional[str] = None
    datum_i_vrijeme_izdavanja: Optional[datetime] = None
    rok_zavrsavanja: Optional[datetime] = None
    status: Optional[str] = None
    vozilo_id: Optional[int] = None
    vozac_id: Optional[int] = None

class RadniNalogOut(RadniNalogBase):
    id: int
    vozilo: VoziloOut
    vozac: VozacOut

    class Config:
        orm_mode = True
