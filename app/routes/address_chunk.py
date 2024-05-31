import uuid

from fastapi import APIRouter, Request, BackgroundTasks, HTTPException

from app.schemas import (
    Generate_AddressChunk_Response,
    Get_AddressChunk_Response,
    Generate_AddressChunk_Request,
)

from app.chains.address_chunk import generate_address_chunk_idea_chain, address_chunks

address_chunk_router = APIRouter(prefix="/address_chunk")


@address_chunk_router.post(
    "/",
    summary="Generate a address_chunk idea.",
    responses={
        201: {"description": "Successfully initiated task."},
    },
)
async def generate_address_chunk(
    r: Generate_AddressChunk_Request, background_tasks: BackgroundTasks
) -> Generate_AddressChunk_Response:
    """Initiates a address_chunk generation for you."""

    idea_id = uuid.uuid4()
    # background_tasks.add_task(
    #     generate_address_chunk_idea_chain,
    #     idea_id,
    #     r.mailing_address,
    # )
    results = await generate_address_chunk_idea_chain(idea_id,r.mailing_address)
    return Generate_AddressChunk_Response(id=idea_id, completed=False,chunked_mailing_address=results)


@address_chunk_router.get(
    "/{id}",
    summary="Get the generated a address_chunk idea.",
    responses={
        200: {"description": "Successfully fetched address_chunk."},
        404: {"description": "address_chunk not found."},
    },
)
async def get_address_chunk(r: Request, id: uuid.UUID) -> Get_AddressChunk_Response:
    """Returns the address_chunk generation for you."""
    if id in address_chunks:
        vacay = address_chunks[id]
        return Get_AddressChunk_Response(
            id=vacay.id, completed=vacay.completed, idea=vacay.idea
        )
    raise HTTPException(status_code=404, detail="ID not found")