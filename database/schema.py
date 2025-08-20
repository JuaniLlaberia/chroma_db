from .collections import CollectionConfig

COLLECTION_SCHEMAS = {
    "documents": CollectionConfig(
        name="documents",
        description="Documents chunks",
        metadata_schema={
            "embedding_type": "text"
        },
    ),
    "images": CollectionConfig(
        name="images",
        description="Image descriptions embeddings",
        metadata_schema={
            "embedding_type": "image",
            "image_url": "string"
        },
    ),
}