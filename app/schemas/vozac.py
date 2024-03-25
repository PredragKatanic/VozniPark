from pydantic import BaseModel
from datetime import date
from typing import Optional

# Shema za kreiranje novog vozača
class VozacCreate(BaseModel):
    ime: str
    prezime: str
    broj_vozacke_dozvole: str
    datum_isteka_dozvole: date
    kategorije_vozacke_dozvole: str
    kontakt_informacije: str
    ogranicenja_za_voznju: Optional[str] = None
    status: str

# Shema za ažuriranje vozača
class VozacUpdate(BaseModel):
    ime: Optional[str] = None
    prezime: Optional[str] = None
    broj_vozacke_dozvole: Optional[str] = None
    datum_isteka_dozvole: Optional[date] = None
    kategorije_vozacke_dozvole: Optional[str] = None
    kontakt_informacije: Optional[str] = None
    ogranicenja_za_voznju: Optional[str] = None
    status: Optional[str] = None

# Shema za prikaz vozača
class VozacOut(BaseModel):
    id: int
    ime: str
    prezime: str
    broj_vozacke_dozvole: str
    datum_isteka_dozvole: date
    kategorije_vozacke_dozvole: str
    kontakt_informacije: str
    ogranicenja_za_voznju: str
    status: str

    class Config:
        orm_mode = True
