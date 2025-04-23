from fastapi import APIRouter, HTTPException
from src.services.database import get_product_by_query

router = APIRouter()

@router.get("/search")
async def search_products(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    
    products = await get_product_by_query(query)
    
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    
    return {"products": products}