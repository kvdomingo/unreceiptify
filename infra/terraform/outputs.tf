output "cognitive_services_endpoint" {
  value = azurerm_cognitive_account.default.endpoint
}

output "cognitive_services_access_key" {
  value     = azurerm_cognitive_account.default.primary_access_key
  sensitive = true
}
