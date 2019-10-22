resource "azurerm_data_factory" "lineage" {
  name                = "${var.data_factory_name}"
  location            = "${azurerm_resource_group.this.location}"
  resource_group_name = "${azurerm_resource_group.this.name}"
}

resource "azurerm_data_factory_pipeline" "lineage_copy" {
  name                = "${azurerm_data_factory.lineage.name}-message-post"
  resource_group_name = "${azurerm_resource_group.this.name}"
  data_factory_name   = "${azurerm_data_factory.lineage.name}"
}