import uuid
from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from app.schemas import address_chunk_schema
from app.schemas import Get_AddressChunk_Response
from loguru import logger


address_chunks = {}

async def generate_address_chunk_idea_chain(
    id: uuid.UUID, mailing_address: str
):
    logger.info(f"idea generation starting for {id}")
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    system_template = """
    I need help with extracting key fields from a mailing address. The key fields to be extracted are street_address,city,state_province_region,postal_code,country. If there are missing fields keep them blank string. Only give me the extracted key fields as output and no other filler text
    
    The mailing address is {mailing_address}.
    """
    address_chunks[id] = address_chunk_schema(id=id, completed=False,chunked_mailing_address="")

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = "{mailing_address_request}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    request = chat_prompt.format_prompt(
        mailing_address=mailing_address,
        # hobbies=hobbies,
        mailing_address_request="help with extracting key fields from a mailing address",
    ).to_messages()
    result = chat(request)
    logger.info(f"Output is {result.content}")

    address_chunks[id].chunked_mailing_address = result.content
    logger.info(f"Completed idea generation for {id} and idea is {address_chunks[id].chunked_mailing_address}")
    return result.content