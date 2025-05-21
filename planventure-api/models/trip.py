from datetime import datetime, timezone
from app import db
from sqlalchemy import JSON

class Trip(db.Model):
    """Trip model for storing travel plans"""
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    itinerary = db.Column(JSON)  # Changed from JSONB to JSON
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), 
                          onupdate=lambda: datetime.now(timezone.utc))

    # Relationship with User model
    user = db.relationship('User', back_populates='trips')

    def to_dict(self):
        """Convert trip object to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'destination': self.destination,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'itinerary': self.itinerary,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __repr__(self):
        return f'<Trip {self.destination}>'