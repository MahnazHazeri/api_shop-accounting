import uuid
from datetime import datetime, timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID, String, DateTime,text
from sqlalchemy.orm import Mapped, Synonym, mapped_column
from sqlalchemy import Enum as TYPEEnum

from src.models.type.enum_type import RoleType


#========================کاربر سیستم=========================


class User(UpdatableDeletableAdminEntity):
    __tablename__ = "users"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("id")

    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[RoleType] = mapped_column(TYPEEnum,default=RoleType.ADMIN)
    is_active: Mapped[bool] = mapped_column(default=True, server_default=text("true"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
