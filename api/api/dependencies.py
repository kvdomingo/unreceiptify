from azure.ai.documentintelligence.aio import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from ollama import AsyncClient

from api.settings import settings

ollama_client = AsyncClient(host=str(settings.OLLAMA_URL))

doc_intel_client = DocumentIntelligenceClient(
    endpoint=settings.AZURE_AI_ENDPOINT,
    credential=AzureKeyCredential(settings.AZURE_AI_ACCESS_KEY),
)
