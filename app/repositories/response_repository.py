from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from database.models.response import Response
from utils.repository import SQLAlchemyRepository


class ResponseRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_response(self, signal_strength: int, mac_address: str|None) -> Response:
        response = Response(signal_strength=signal_strength, mac_address=mac_address)
        self.session.add(response)
        self.session.commit()
        self.session.refresh(response)
        return response

    def get_last_response(self) -> Response:
        return self.session.query(Response).order_by(Response.created_at.desc()).first()

    def get_avg_signal_strength_last_24_hours(self) -> float:
        twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
        avg_signal_strength = self.session.query(func.avg(Response.signal_strength)).filter(Response.created_at >= twenty_four_hours_ago).scalar()
        return avg_signal_strength
