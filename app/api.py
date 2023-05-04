"""Define the API schema."""
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ConversationRequest(BaseModel):
    """Request message to the Carplus Chatbot."""

    # Message is passed directly to the Chatbot
    # deployed in the plugin.
    message: str


class ConversationResponse(BaseModel):
    """Deployed Carplus Chatbot response."""

    response: str

class CarModel(str, Enum):
    """CarModel of Carplus's store"""
    Nissan_Sentra = "Nissan_Sentra"
    Nissan_Tiida = "Nissan_Tiida"

class Location(str, Enum):
    """Location of Carplus's store."""
    新店門市 = "新店門市"
    板橋門市 = "板橋門市"

class ReserveURLRequest(BaseModel):
    """ Request message to make reservation via Carplus's Website."""
    car_model: Optional[CarModel] = "Nissan Sentra"
    pickup_date: Optional[str] = None  # any date string format
    return_date: Optional[str] = None  # any date string format
    pickup_store: Location = "新店門市"
    return_store: Location = "板橋門市"

class ReserveURLResponse(BaseModel):
    """ Request message to make reservation via Carplus's Website."""
    response: str