from pydantic import BaseModel
from datetime import date
from typing import Optional

# Shema za kreiranje novog vozila
class VoziloCreate(BaseModel):
    marka: str
    model: str
    registracijski_broj: str
    datum_isteka_registracije: date
    godina_proizvodnje: int
    tip_goriva: str  # Možete koristiti Enum ako želite striktnu validaciju
    status: str

# Shema za ažuriranje vozila
class VoziloUpdate(BaseModel):
    marka: Optional[str] = None
    model: Optional[str] = None
    registracijski_broj: Optional[str] = None
    datum_isteka_registracije: Optional[date] = None
    godina_proizvodnje: Optional[int] = None
    tip_goriva: Optional[str] = None
    status: Optional[str] = None

# Shema za prikaz vozila
class VoziloOut(BaseModel):
    id: int
    marka: str
    model: str
    registracijski_broj: str
    datum_isteka_registracije: date
    godina_proizvodnje: int
    tip_goriva: str
    status: str

    class Config:
        orm_mode = True
