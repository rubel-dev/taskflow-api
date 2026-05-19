from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        db 
        yield
    finally:
        db.close()