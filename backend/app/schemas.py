from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, HttpUrl


ShortText = Annotated[str, Field(min_length=1, max_length=140)]


class ProjectBase(BaseModel):
    title: ShortText
    category: Annotated[str, Field(min_length=1, max_length=80)]
    description: Annotated[str, Field(min_length=1, max_length=600)]
    image_url: HttpUrl
    technologies: list[Annotated[str, Field(min_length=1, max_length=40)]] = Field(default_factory=list, max_length=12)
    case_study_url: HttpUrl | None = None
    live_url: HttpUrl | None = None
    sort_order: int = Field(default=0, ge=0, le=9999)
    is_featured: bool = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectOut(ProjectBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SkillBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=80)]
    logo_url: HttpUrl
    sort_order: int = Field(default=0, ge=0, le=9999)
    is_active: bool = True


class SkillCreate(SkillBase):
    pass


class SkillUpdate(SkillBase):
    pass


class SkillOut(SkillBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TokenCheck(BaseModel):
    ok: bool


EmailText = Annotated[str, Field(min_length=5, max_length=254, pattern=r"^[^\s@]+@[^\s@]+\.[^\s@]+$")]


class ContactMessageCreate(BaseModel):
    name: ShortText
    email: EmailText
    message: Annotated[str, Field(min_length=1, max_length=2000)]


class ContactMessageOut(ContactMessageCreate):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
