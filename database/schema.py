from .collections import CollectionConfig

COLLECTION_SCHEMAS = {
    "documents": CollectionConfig(
        name="documents",
        description="",
        metadata_schema={},
        chunk_size=750,
        chunk_overlap=100
    ),
}