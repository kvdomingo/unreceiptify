terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.11.0"
    }
  }

  backend "azurerm" {
    key = "unreceiptify"
  }
}
