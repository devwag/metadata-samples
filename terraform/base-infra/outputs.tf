output "base_resource_group_name" {
  value = "${azurerm_resource_group.this.name}"
}

output "base_user_assigned_identity_name" {
  value = "${azurerm_user_assigned_identity.this.name}"
}

output "base_storage_account_name" {
  value = "${azurerm_storage_account.this.name}"
}

output "base_vnet_name" {
  value = "${azurerm_virtual_network.this.name}"
}

output "base_keyvault_name" {
  value = "${azurerm_key_vault.this.name}"
}

output "base_acr_name" {
  value = "${azurerm_container_registry.this.name}"
}
