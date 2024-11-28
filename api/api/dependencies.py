from azure.ai.documentintelligence.aio import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

from api.settings import settings

doc_intel_client = DocumentIntelligenceClient(
    endpoint=settings.AZURE_AI_ENDPOINT,
    credential=AzureKeyCredential(settings.AZURE_AI_ACCESS_KEY),
)
