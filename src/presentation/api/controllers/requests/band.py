from pydantic.main import BaseModel


class BaseBand(BaseModel):
    title: str


class CreateBandRequest(BaseBand):
    pass


class UpdateBandRequest(BaseBand):
    id: int
    title: str | None


class UpdateMusicianBandRequest(BaseModel):
    musician_id: int | None = None
