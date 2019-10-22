variable "resource_group_name" {
  description = "Name of resource group"
  type        = "string"
}

variable "location" {
  description = "Location of resources"
  type        = "string"
  default     = "East US2"
}

variable "sql_username" {
  description = "Login username for SQL server"
  type        = "string"
}

variable "sql_password" {
  description = "Login password for SQL server"
  type        = "string"
}

variable "adls_name" {
  description = "Azure DataLake storage name. Can only contain lowercase letters & numbers."
  type        = "string"
}

variable "acr_name" {
  description = "Azure Container Registry name. Can only contain alpha numeric characters"
  type        = "string"
}

variable "keyvault_name" {
  description = "Name of key vault"
  type = "string"
}