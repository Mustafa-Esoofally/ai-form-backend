import uuid
from fastapi import APIRouter, Request, BackgroundTasks, HTTPException
from app.schemas import (
    Generate_Save_Address_Response,
    Get_Save_Address_Response,
    Generate_Save_Address_Request,
)
import chromadb
# from app.chains.save_address import generate_save_address_idea_chain, save_addresss

save_address_router = APIRouter(prefix="/save_address")


# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Define your collection
address_collection = chroma_client.create_collection(name="mailing_addresses")

@save_address_router.post(
    "/",
    summary="Generate a save_address idea.",
    responses={
        201: {"description": "Successfully initiated task."},
    },
)
async def generate_save_address(
    r: Generate_Save_Address_Request, background_tasks: BackgroundTasks
) -> Generate_Save_Address_Response:
    """Initiates a save_address generation for you."""
    print("line 27")    
    address_id = uuid.uuid4()
    # background_tasks.add_task(
    #     generate_save_address_idea_chain,
    #     idea_id,
    #     r.mailing_address,
    # )
    # results = await generate_save_address_idea_chain(idea_id,r.mailing_address)
    print("line 49")
    print(type(r))
    print(r)
    print(r.final_mailing_address)
    metadata_insert = {
        "street_address": r.street_address, 
        "city": r.city,
        "state_province_region":  r.state_province_region,
        "postal_code": r.postal_code, 
        "country": r.country 
    }
    address_collection.add(
        documents=[r.final_mailing_address],
        metadatas=[metadata_insert],
        ids=[str(address_id)]
    )
    return Generate_Save_Address_Response(id=address_id, completed=False)


@save_address_router.get(
    "/{id}",
    summary="Get the generated a save_address idea.",
    responses={
        200: {"description": "Successfully fetched save_address."},
        404: {"description": "save_address not found."},
    },
)
async def get_save_address(r: Request, id: uuid.UUID) -> Get_Save_Address_Response:
    """Returns the save_address generation for you."""
    if id in save_addresss:
        vacay = save_addresss[id]
        return Get_Save_Address_Response(
            id=vacay.id, completed=vacay.completed, idea=vacay.idea
        )
    raise HTTPException(status_code=404, detail="ID not found")