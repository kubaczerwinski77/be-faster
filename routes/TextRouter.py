from fastapi import APIRouter
from controllers.TextController import Text
from models.TextModels import TextReq, TextRes

router = APIRouter(
  prefix="/texts",
  tags=["texts"]
)

initText = Text()

@router.post("/", tags=["texts"], response_model=TextRes)
async def generate_text(params: TextReq):
  doc = await initText.create_text(params)
  return doc

@router.get("/{id}", response_model=TextRes)
async def get_text_by_id(id):
  doc = await initText.fetch_text_by_id(id)
  return doc
