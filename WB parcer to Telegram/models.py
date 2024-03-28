from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    reviewRating: float
    supplierId: int
    root: int
    feedback_count: int = None
    valuation: str = None


class Items(BaseModel):
    products: list[Item]


class Review(BaseModel):
    user_info: set
    text: str


class Feedback(BaseModel):
    feedbackCountWithText: int
    valuation: str
    feedbacks: list[Review]
