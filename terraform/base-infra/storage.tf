locals {
  unique_id = "${substr(md5(var.resource_group_name), 0, 8)}"
}

resource "azurerm_storage_account" "this" {
  name                     = "${join("", ["storage", local.unique_id])}"
  resource_group_name      = "${azurerm_resource_group.this.name}"
  location                 = "${var.location}"
  account_kind             = "StorageV2"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = "true"

  # Associates SA under VNet
  network_rules {
    # Allow for now as trying to add ADLS Gen2 after network rule is in place denies request from outside IP
    default_action             = "Allow"
    bypass                     = ["AzureServices"]
    virtual_network_subnet_ids = ["${azurerm_subnet.this.id}"]
  }
}

resource "azurerm_storage_data_lake_gen2_filesystem" "this" {
  name               = "${azurerm_resource_group.this.name}"
  storage_account_id = azurerm_storage_account.this.id
}

resource "azurerm_sql_server" "base" {
  name                         = "${azurerm_resource_group.this.name}-base"
  resource_group_name          = "${azurerm_resource_group.this.name}"
  location                     = "${var.location}"
  version                      = "12.0"
  administrator_login          = "${var.sql_username}"
  administrator_login_password = "${var.sql_password}"
}

resource "azurerm_sql_database" "base_db" {
  name                = "${azurerm_resource_group.this.name}-base-db"
  resource_group_name = "${azurerm_resource_group.this.name}"
  location            = "${var.location}"
  server_name         = "${azurerm_sql_server.base.name}"
}

resource "azurerm_sql_database" "base_dw" {
  name                             = "${azurerm_resource_group.this.name}-base-dw"
  resource_group_name              = "${azurerm_resource_group.this.name}"
  location                         = "${var.location}"
  server_name                      = "${azurerm_sql_server.base.name}"
  edition                          = "DataWarehouse"
  requested_service_objective_name = "DW100c"
}

resource "azurerm_sql_virtual_network_rule" "vnet_sql_association" {
  name                = "${azurerm_sql_server.base.name}-vnet-rule"
  resource_group_name = "${azurerm_resource_group.this.name}"
  server_name         = "${azurerm_sql_server.base.name}"
  subnet_id           = "${azurerm_subnet.this.id}"
}
