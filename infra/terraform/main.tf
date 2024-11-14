provider "azurerm" {
  subscription_id = var.subscription_id

  features {}
}

locals {
  region = "West US2"
}

resource "azurerm_resource_group" "default" {
  name     = "unreceiptify-rg"
  location = local.region
}

resource "azurerm_cognitive_account" "default" {
  name                = "cognitive-services-account"
  location            = local.region
  kind                = "CognitiveServices"
  sku_name            = "S0"
  resource_group_name = azurerm_resource_group.default.name
}
