resource "azurerm_databricks_workspace" "this" {
  name                = "${var.databricks_name}"
  resource_group_name = "${azurerm_resource_group.this.name}"
  location            = "${azurerm_resource_group.this.location}"
  sku                 = "standard"
}

data "azurerm_virtual_network" "databricks" {
  name                = "workers-vnet"
  resource_group_name = "${regex("resourceGroups/([^/]+)$", azurerm_databricks_workspace.this.managed_resource_group_id)[0]}"
}

resource "azurerm_virtual_network_peering" "vnet-to-databricks" {
  name                      = "vnet-to-databricks-peer"
  resource_group_name       = "${data.azurerm_virtual_network.base.resource_group_name}"
  virtual_network_name      = "${data.azurerm_virtual_network.base.name}"
  remote_virtual_network_id = "${data.azurerm_virtual_network.databricks.id}"
}
