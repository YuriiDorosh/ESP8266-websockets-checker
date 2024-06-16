from sqlalchemy.orm import Session
from database.models.user import User
from utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_user(
        self,
        telegram_tag: str,
        telegram_id: int,
        first_name: str = None,
        last_name: str = None,
        is_admin: bool = False,
    ) -> User:
        user = User(
            telegram_tag=telegram_tag,
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            is_admin=is_admin,
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_all_telegram_ids(self) -> list[int]:
        return [user.telegram_id for user in self.session.query(User.telegram_id).all()]
