from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

import logging
from pydantic import BaseModel
from typing import Dict, Any, List

from app.algorithm.stock_distribution import distribute_stocks


class Investor(BaseModel):
    name: str
    requested_amount: int
    average_amount: int


class Investment(BaseModel):
    allocation_amount: int
    investor_amounts: List[Investor]


app = FastAPI(
    title="Stock Distribution app",
    description="provides api for allocation proration",
    version="0.1",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "Please 'Post' instead of 'Get' on this endpoint to process stocks. For more info go to /docs "}


@app.get("/alive")
async def alive():
    return "Yes"

@app.post("/", name="stocks")
async def stocks(investment: Investment):
    logging.info('Parsing investment')
    # Model is used manily for input validation and quicker results
    # I've tranforming model back to json to prevent abstraction leakage
    return distribute_stocks(jsonable_encoder(investment))
