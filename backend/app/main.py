from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .config import get_settings
from .database import engine, get_session
from .models import Base, ContactMessage, Project, Skill
from .schemas import (
    ContactMessageCreate,
    ContactMessageOut,
    ProjectCreate,
    ProjectOut,
    ProjectUpdate,
    SkillCreate,
    SkillOut,
    SkillUpdate,
    TokenCheck,
)
from .security import RateLimitMiddleware, SecurityHeadersMiddleware, require_admin


settings = get_settings()
app = FastAPI(title="Portfolio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "X-Admin-Token"],
)
app.add_middleware(
    RateLimitMiddleware,
    max_requests=settings.rate_limit_requests,
    window_seconds=settings.rate_limit_window_seconds,
)
app.add_middleware(SecurityHeadersMiddleware)


@app.on_event("startup")
async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root() -> dict[str, str]:
    return {"name": "Portfolio API", "status": "ok", "health": "/api/health"}


@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/admin/check-token", response_model=TokenCheck, dependencies=[Depends(require_admin)])
async def check_token() -> TokenCheck:
    return TokenCheck(ok=True)


@app.get("/api/projects", response_model=list[ProjectOut])
async def list_projects(session: AsyncSession = Depends(get_session)) -> list[Project]:
    result = await session.execute(
        select(Project).where(Project.is_featured.is_(True)).order_by(Project.sort_order.asc(), Project.created_at.desc())
    )
    return list(result.scalars().all())


@app.get("/api/admin/projects", response_model=list[ProjectOut], dependencies=[Depends(require_admin)])
async def list_admin_projects(session: AsyncSession = Depends(get_session)) -> list[Project]:
    result = await session.execute(select(Project).order_by(Project.sort_order.asc(), Project.created_at.desc()))
    return list(result.scalars().all())


@app.post(
    "/api/admin/projects",
    response_model=ProjectOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
async def create_project(payload: ProjectCreate, session: AsyncSession = Depends(get_session)) -> Project:
    project = Project(**payload.model_dump(mode="json"))
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project


@app.put("/api/admin/projects/{project_id}", response_model=ProjectOut, dependencies=[Depends(require_admin)])
async def update_project(project_id: str, payload: ProjectUpdate, session: AsyncSession = Depends(get_session)) -> Project:
    project = await session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    for key, value in payload.model_dump(mode="json").items():
        setattr(project, key, value)

    await session.commit()
    await session.refresh(project)
    return project


@app.delete("/api/admin/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_admin)])
async def delete_project(project_id: str, session: AsyncSession = Depends(get_session)) -> None:
    project = await session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    await session.delete(project)
    await session.commit()


@app.get("/api/skills", response_model=list[SkillOut])
async def list_skills(session: AsyncSession = Depends(get_session)) -> list[Skill]:
    result = await session.execute(
        select(Skill).where(Skill.is_active.is_(True)).order_by(Skill.sort_order.asc(), Skill.created_at.desc())
    )
    return list(result.scalars().all())


@app.get("/api/admin/skills", response_model=list[SkillOut], dependencies=[Depends(require_admin)])
async def list_admin_skills(session: AsyncSession = Depends(get_session)) -> list[Skill]:
    result = await session.execute(select(Skill).order_by(Skill.sort_order.asc(), Skill.created_at.desc()))
    return list(result.scalars().all())


@app.post("/api/contact/messages", response_model=ContactMessageOut, status_code=status.HTTP_201_CREATED)
async def create_contact_message(payload: ContactMessageCreate, session: AsyncSession = Depends(get_session)) -> ContactMessage:
    message = ContactMessage(**payload.model_dump(mode="json"))
    session.add(message)
    await session.commit()
    await session.refresh(message)
    return message


@app.get("/api/admin/contact-messages", response_model=list[ContactMessageOut], dependencies=[Depends(require_admin)])
async def list_contact_messages(session: AsyncSession = Depends(get_session)) -> list[ContactMessage]:
    result = await session.execute(select(ContactMessage).order_by(ContactMessage.created_at.desc()))
    return list(result.scalars().all())


@app.post(
    "/api/admin/skills",
    response_model=SkillOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
async def create_skill(payload: SkillCreate, session: AsyncSession = Depends(get_session)) -> Skill:
    skill = Skill(**payload.model_dump(mode="json"))
    session.add(skill)
    try:
        await session.commit()
    except IntegrityError as exc:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Skill name already exists") from exc
    await session.refresh(skill)
    return skill


@app.put("/api/admin/skills/{skill_id}", response_model=SkillOut, dependencies=[Depends(require_admin)])
async def update_skill(skill_id: str, payload: SkillUpdate, session: AsyncSession = Depends(get_session)) -> Skill:
    skill = await session.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")

    for key, value in payload.model_dump(mode="json").items():
        setattr(skill, key, value)

    try:
        await session.commit()
    except IntegrityError as exc:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Skill name already exists") from exc
    await session.refresh(skill)
    return skill


@app.delete("/api/admin/skills/{skill_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(require_admin)])
async def delete_skill(skill_id: str, session: AsyncSession = Depends(get_session)) -> None:
    skill = await session.get(Skill, skill_id)
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")

    await session.delete(skill)
    await session.commit()
