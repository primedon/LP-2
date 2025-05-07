def recommend_storage(data_type):
    if data_type == "text":
        return "Use a relational database like MySQL."
    elif data_type == "image":
        return "Use cloud object storage like AWS S3 or Google Cloud Storage."
    elif data_type == "video":
        return "Use a media server with CDN support (e.g., AWS MediaConvert)."
    elif data_type == "document":
        return "Use a document management system like SharePoint or Google Drive."
    else:
        return "Unknown data type."

# --- Example Usage ---
data_type = input("Enter data type (text/image/video/document): ").lower()
print(recommend_storage(data_type))