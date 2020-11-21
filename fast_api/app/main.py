from fastapi import FastAPI
from .tags import tags
from .events import events
from .polls import polls

from .db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# async def get_token_header(x_token: str = Header(...)):
#    if x_token != "fake-super-secret-token":
#        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    tags.router,
    prefix='/tags',
    tags=['tags'],
    responses={500: {"description": "Error: Check server logs"}}
)
app.include_router(
    events.router,
    prefix='/events',
    tags=['events'],
    responses={500: {"description": "Error: Check server logs"}}
)
app.include_router(
    polls.router,
    prefix='/polls',
    tags=['polls'],
    responses={500: {"description": "Error: Check server logs"}}
)
# dependencies=[Depends(get_token_header)],
# responses={404: {"description": "Not found"}},
# )
