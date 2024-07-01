from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class URL(db.Model):
    """Database model for storing URLs."""
    id_ = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1000)) 
    shortcode = db.Column(db.String(6), unique=True, nullable=False) # 6 max ch, unique ensures that 2 shortcode cant match, nullable ensures that it is  not required
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    last_redirect = db.Column(db.DateTime)
    redirect_count = db.Column(db.Integer, default=0)

