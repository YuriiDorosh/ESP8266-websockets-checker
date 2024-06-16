from datetime import datetime, timedelta

from database.models.wifi import Wifi
from sqlalchemy.orm import Session

from utils.repository import SQLAlchemyRepository


class WifiRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_wifi_record(self, is_powered: bool) -> Wifi:
        wifi = Wifi(is_powered=is_powered)
        self.session.add(wifi)
        self.session.commit()
        self.session.refresh(wifi)
        return wifi

    def get_last_wifi_record(self) -> Wifi:
        return self.session.query(Wifi).order_by(Wifi.created_at.desc()).first()

    def get_wifi_records_last_24_hours(self) -> list[Wifi]:
        twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
        return (
            self.session.query(Wifi)
            .filter(Wifi.created_at >= twenty_four_hours_ago)
            .all()
        )

    def get_wifi_records_last_week(self) -> list[Wifi]:
        one_week_ago = datetime.now() - timedelta(weeks=1)
        return self.session.query(Wifi).filter(Wifi.created_at >= one_week_ago).all()
