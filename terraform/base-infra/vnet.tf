resource "azurerm_virtual_network" "this" {
  name                = "${azurerm_resource_group.this.name}-basevnet"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.this.name}"
  address_space       = ["10.7.29.0/29"]
}

resource "azurerm_subnet" "this" {
  name                 = "${azurerm_resource_group.this.name}-base"
  resource_group_name  = "${azurerm_resource_group.this.name}"
  virtual_network_name = "${azurerm_virtual_network.this.name}"
  address_prefix       = "10.7.29.0/29"
  service_endpoints    = ["Microsoft.KeyVault", "Microsoft.Sql", "Microsoft.Storage", "Microsoft.Web"]
}


