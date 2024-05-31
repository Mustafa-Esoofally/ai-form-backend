
from pydantic import BaseModel, Field
from typing import List
import uuid


class Generate_AddressChunk_Response(BaseModel):
    id: uuid.UUID = Field(description="ID Of the generated idea")
    completed: bool = Field(
        description="Flag indicating if the generation was completed"
    )
    chunked_mailing_address: str = Field(
        description="Flag indicating if the generation was completed"
    ) 


class Get_AddressChunk_Response(Generate_AddressChunk_Response):
    # idea: str = Field(description="The generated idea")
    street_address: str = Field()
    city: str = Field()
    state_province_region: str = Field()
    postal_code: int = Field()
    country: str = Field()


class Generate_AddressChunk_Request(BaseModel):
    mailing_address: str = Field(description="Your favorite season")

class address_chunk_schema(Generate_AddressChunk_Response):
    # idea: str = Field(description="The generated idea")
    chunked_mailing_address: str = Field(description="The generated idea")
    
 
 
 
class Generate_Save_Address_Response(BaseModel):
    id: uuid.UUID = Field(description="ID Of the generated idea")
    completed: bool = Field(
        description="Flag indicating if the generation was completed"
    ) 

class Get_Save_Address_Response(Generate_Save_Address_Response):
    # idea: str = Field(description="The generated idea")
    final_mailing_address: str = Field(description="Your favorite season")


class Generate_Save_Address_Request(BaseModel):
    final_mailing_address: str = Field(description="Your favorite season")
    street_address: str = Field()
    city: str = Field()
    state_province_region: str = Field()
    postal_code: int = Field()
    country: str = Field()

class save_address_schema(Generate_Save_Address_Response):
    final_mailing_address: str = Field(description="The generated idea")
    street_address: str = Field()
    city: str = Field()
    state_province_region: str = Field()
    postal_code: int = Field()
    country: str = Field()    