from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sdfghj_Backend_Api API",
    description="Generated from Impact Analysis specifications",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "endpoints": 15,
        "models": 7
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "sdfghj_backend_api"}

# Generated API endpoints
@app.get("/api/users")
def api_users(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.get("/api/users/{id}")
def api_users_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/users")
def api_users(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/api/users/{id}")
def api_users_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/api/users/{id}")
def api_users_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/api/hotels")
def api_hotels(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.get("/api/hotels/{id}")
def api_hotels_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/hotels")
def api_hotels(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/api/hotels/{id}")
def api_hotels_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/api/hotels/{id}")
def api_hotels_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/api/bookings")
def api_bookings(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.get("/api/bookings/{id}")
def api_bookings_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/bookings")
def api_bookings(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/api/bookings/{id}")
def api_bookings_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/api/bookings/{id}")
def api_bookings_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
